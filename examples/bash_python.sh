#!/bin/sh
# Polyglot: valid Bash AND valid Python
# Run as bash:   bash bash_python.sh
# Run as Python: python3 bash_python.sh

"exec" "python3" "$0" "$@"

# ── Python only executes below this line ──────────────────────
# Bash never reaches here — it was replaced by python3 via exec.

import sys

print("Hello from Python!")
print(f"Python {sys.version_info.major}.{sys.version_info.minor} — interpreted.")
print()
print("How it works:")
print('  Bash:   "exec" is a quoted builtin → replaces shell with python3')
print('  Python: "exec" "python3" "$0" "$@" = adjacent string literals')
print('          They concatenate to one big string, then get discarded.')
print("          Python sees no exec — just continues past it.")
