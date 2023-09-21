import sys

A, B = map(int, sys.stdin.readline().split())

A, B = int('1' * A), int('1' * B)ㅑ
while A % B != 0:
    A, B = B, A % B
print(B)
