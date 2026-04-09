#if 0
# ── POLYGLOT FILE ─────────────────────────────────────────────
# Valid C source AND valid Python script — same bytes, two runtimes
#
# Run as Python:   python demo.c
# Compile as C:    gcc demo.c -o demo && ./demo
#
# How it works:
#   C preprocessor:  #if 0 ... #endif blocks are stripped before compilation.
#   Python parser:   #if 0 is just a comment; x = """...""" hides the C code
#                    inside a Python string, so Python never executes it.
# ──────────────────────────────────────────────────────────────
x = """
#endif

#include <stdio.h>

int main(void) {
    printf("Hello from C!\n");
    printf("Compiled to native machine code.\n");
    return 0;
}

#if 0
"""
# ── Python only sees below this line ──────────────────────────
# Everything above (the C code) was quietly assigned to the
# string variable x.  Python never tried to execute any of it.

print("Hello from Python!")
print("Interpreted line by line.")

#endif
