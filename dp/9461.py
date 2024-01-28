import sys

T = int(sys.stdin.readline())

dp = [1, 1, 1, 2, 2] + [0] * 95
for i in range(5, 100):
    dp[i] = dp[i - 5] + dp[i - 1]

for _ in range(T):
    print(dp[int(sys.stdin.readline()) - 1])
