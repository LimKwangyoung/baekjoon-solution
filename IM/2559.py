import sys

N, K = map(int, sys.stdin.readline().split())
temps = list(map(int, sys.stdin.readline().split()))

result = cur = sum(temps[0:0 + K])
for i in range(N - K):
    cur = cur - temps[i] + temps[i + K]
    result = max(result, cur)
print(result)
