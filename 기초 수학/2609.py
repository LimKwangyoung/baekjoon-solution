import sys


def find_gcd(num1: int, num2: int) -> int:
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return num2


A, B = map(int, sys.stdin.readline().split())

gcd = find_gcd(A, B)
lcm = A * B // gcd
print(gcd)
print(lcm)
