import os
import re
from flask import Flask, render_template, send_from_directory
import markdown

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXAMPLES_DIR = os.path.join(BASE_DIR, '..', 'examples')
SLIDES_MD_PATH = os.path.join(BASE_DIR, 'slides.md')


def read_example(filename):
    path = os.path.join(EXAMPLES_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def read_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def parse_front_matter(content):
    default_meta = {
        'title': 'Polyglot Programming - HacKSU',
        'show_logo': 'true',
    }

    if not content.startswith('---\n'):
        return default_meta, content

    end = content.find('\n---\n', 4)
    if end == -1:
        return default_meta, content

    block = content[4:end]
    body = content[end + 5:]

    meta = dict(default_meta)
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith('#') or ':' not in line:
            continue
        key, value = line.split(':', 1)
        meta[key.strip()] = value.strip()

    return meta, body


def markdown_to_html(text):
    return markdown.markdown(
        text,
        extensions=['fenced_code', 'tables', 'sane_lists', 'nl2br'],
    )


def extract_first_heading(markdown_text):
    for line in markdown_text.splitlines():
        m = re.match(r'^#{1,6}\s+(.+?)\s*$', line.strip())
        if m:
            return m.group(1)
    return ''


def load_slides():
    raw = read_text(SLIDES_MD_PATH)
    meta, body = parse_front_matter(raw)

    raw_slides = [s.strip() for s in re.split(r'\n---\s*\n', body) if s.strip()]
    slides = []
    for i, source in enumerate(raw_slides, start=1):
        heading = extract_first_heading(source)
        slides.append({
            'id': f'slide-{i}',
            'tag': f'{i:02d}',
            'title': heading or f'Slide {i}',
            'html': markdown_to_html(source),
        })

    return meta, slides


@app.route('/')
def index():
    deck_meta, slides = load_slides()

    return render_template(
        'index.html',
        deck_title=deck_meta.get('title', 'Polyglot Programming - HacKSU'),
        show_logo=deck_meta.get('show_logo', 'true').lower() not in {'false', '0', 'no'},
        slides=slides,
        demo_c=read_example('demo.c'),
        bash_python=read_example('bash_python.sh'),
    )


@app.route('/logo')
def logo():
    return send_from_directory(BASE_DIR, 'HacKSU.png')


if __name__ == '__main__':
    print("Starting polyglot presentation at http://localhost:5000")
    app.run(debug=True, port=5000)
