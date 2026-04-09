# Polyglot Programming

> One file. Many languages. One runtime won't tell you.

A CS lecture on polyglot files — single files that are simultaneously valid in multiple languages or formats.

## Structure

```
examples/
  demo.c           C + Python polyglot (the main demo)
  bash_python.sh   Bash + Python polyglot

presentation/
  app.py           Flask slide deck server
  requirements.txt
  templates/
    index.html     12-slide terminal-aesthetic presentation
```

## Running the demos

```bash
# C + Python polyglot
python examples/demo.c
gcc examples/demo.c -o demo && ./demo

# Bash + Python polyglot
bash    examples/bash_python.sh
python3 examples/bash_python.sh
```

## Running the presentation

```bash
cd presentation
pip install -r requirements.txt
python app.py
# open http://localhost:5000
```

Navigate slides with **arrow keys**, **Space**, or the on-screen buttons.

## Topics covered

1. What is a polyglot file?
2. How parsers work (ignored regions, skip directives)
3. HTML + CSS + JavaScript — the web is already polyglot
4. Binary polyglots — JPEG+ZIP, GIFAR, PDF+ZIP
5. The C+Python trick — `#if 0` + triple-quoted strings
6. Live demo — `examples/demo.c`
7. Bash+Python — the quoted exec trick
8. polycompiler — Python+JS (github.com/evanzhoudev/polycompiler)
9. Why it matters — CTF, security, parser literacy, art
10. Exercises
