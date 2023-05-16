import sys

A, B = map(int, sys.stdin.readline().split())

a, b = A, B
while a % b != 0:
    a, b = b, a % b  # b is GCD.
print(A * B // b)
