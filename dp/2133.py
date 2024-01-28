import sys

N = int(sys.stdin.readline())

dp = [0, 0, 3] + [0] * (N - 2)
for i in range(4, N + 1, 2):
    dp[i] = 3 * dp[i - 2] + 2 * sum(dp[:i - 2]) + 2
print(dp[N])
