import sys
import math

# Solution 1 (combination with repetition)
N, K = map(int, sys.stdin.readline().split())

print(math.factorial(K + N - 1) // (math.factorial(N) * math.factorial(K - 1)) % 1000000000)

# Solution 2
N, K = map(int, sys.stdin.readline().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]  # count when N is decomposed into K numbers

for i in range(N + 1):
    for j in range(1, K + 1):
        if i == 0 or j == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(dp[N][K] % 1000000000)

# Solution 3
N, K = map(int, sys.stdin.readline().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]  # count when N is decomposed into K numbers
dp[0][0] = 1

for i in range(N + 1):
    for j in range(1, K + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(dp[N][K] % 1000000000)
