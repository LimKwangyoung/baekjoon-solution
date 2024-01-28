import sys

N = int(sys.stdin.readline())

# count of the last number for 0 and 1.
dp = [0, 1]
for _ in range(2, N + 1):
    dp = [dp[0] + dp[1], dp[0]]
print(sum(dp))
