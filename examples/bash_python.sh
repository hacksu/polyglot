#!/bin/sh
# Polyglot: valid Bash AND valid Python
# Run as bash:   bash bash_python.sh
# Run as Python: python3 bash_python.sh

"exec" "python3" "$0" "$@"

import os, sys, platform

print(f"[python {sys.version_info.major}.{sys.version_info.minor}]")
print(f"  OS:    {platform.system()} {platform.release()}")
print(f"  Shell: {os.environ.get('SHELL', 'unknown')}")
print(f"  File:  {__file__}")
print()
print("Bash hit 'exec python3' and handed off.")
print("Everything above never ran as bash.")
