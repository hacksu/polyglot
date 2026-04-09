import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXAMPLES_DIR = os.path.join(BASE_DIR, '..', 'examples')


def read_example(filename):
    path = os.path.join(EXAMPLES_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


@app.route('/')
def index():
    return render_template(
        'index.html',
        demo_c=read_example('demo.c'),
        bash_python=read_example('bash_python.sh'),
    )


@app.route('/logo')
def logo():
    return send_from_directory(BASE_DIR, 'HacKSU.png')


if __name__ == '__main__':
    print("Starting polyglot presentation at http://localhost:5000")
    app.run(debug=True, port=5000)
