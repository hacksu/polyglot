#if 0
# Run as Python:  python demo.c
# Compile as C:   gcc demo.c -o demo && ./demo
x = """
#endif

#include <stdio.h>

int main(void) {
    printf("[ C ]  Fibonacci: ");
    int a = 0, b = 1;
    for (int i = 0; i < 8; i++) {
        printf("%d ", a);
        int t = a + b; a = b; b = t;
    }
    printf("\n");
    return 0;
}

#if 0
"""
print("[ Python ]  Fibonacci: ", end="")
a, b = 0, 1
for _ in range(8):
    print(a, end=" ")
    a, b = b, a + b
print()

#endif
