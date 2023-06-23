import sys
import math

N = int(sys.stdin.readline())
dp = [i for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - j**2] + 1)
print(dp[-1])
