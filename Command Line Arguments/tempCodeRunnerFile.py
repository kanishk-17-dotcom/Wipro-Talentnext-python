# Q.1 Write a program to accept two numbers as command line arguments and display their sum.

import sys
if len(sys.argv) != 3:
    print("Usage: python num1 num2")
    sys.exit()
a = int(sys.argv[1])
b = int(sys.argv[2])
c = a + b
print("Sum =", c)