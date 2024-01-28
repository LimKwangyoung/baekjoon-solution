import sys

T = int(sys.stdin.readline())

dp = [0, 1, 2, 4] + [0] * 8
for i in range(4, 12):
    # cases for starting at 3, 2, and 1.
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for _ in range(T):
    print(dp[int(sys.stdin.readline())])
