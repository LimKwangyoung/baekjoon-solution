X = int(input())
N = int(input())

result = 0
for _ in range(N):
    a, b = map(int, input().split())
    result += a * b
print('Yes' if X == result else 'No')