import sys

n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n)]

dp = [[0] * m for _ in range(n)]
result = 0
for row in range(n):
    for col in range(m):
        if board[row][col] == '0':
            continue
        dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1
        result = max(result, dp[row][col]**2)
print(result)
