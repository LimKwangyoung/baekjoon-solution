import sys

N = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = float('inf')
for start in range(3):
    dp = [[float('inf')] * 3 for _ in range(N)]
    dp[0][start] = costs[0][start]
    for i in range(1, N):
        dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
    result = min(result, min(dp[-1]))
print(result)
