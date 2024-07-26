import sys
import collections

N, D = map(int, sys.stdin.readline().split())

info = collections.defaultdict(list)
for _ in range(N):
    src, dst, length = map(int, sys.stdin.readline().split())
    if not (D < dst or dst - src < length):
        info[dst].append([src, length])

dp = [float('inf')] * (D + 1)
dp[0] = 0
for dst in range(1, D + 1):
    dp[dst] = dp[dst - 1] + 1
    if dst in info:
        for src, length in info[dst]:
            dp[dst] = min(dp[dst], dp[src] + length)
print(dp[-1])
