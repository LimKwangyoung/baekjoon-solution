import sys

n = int(sys.stdin.readline())

num1, num2 = 1, 1
for _ in range(2, n + 1):
    num1, num2 = num2, 2 * num1 + num2
print(num2 % 10007)
