import sys


def find_gcd(num1: int, num2: int) -> int:
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return num2


A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

gcd = find_gcd(B, D)
numerator, denominator = A * (D // gcd) + C * (B // gcd), B * D // gcd

gcd = find_gcd(numerator, denominator)
print(numerator // gcd, denominator // gcd)
