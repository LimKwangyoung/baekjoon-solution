import sys

N = int(sys.stdin.readline())
milk = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
if not milk[0][0]:
    dp[0][0] = 1

for row in range(N):
    for col in range(N):
        for r, c in ((row - 1, col), (row, col - 1)):
            if 0 <= r < N and 0 <= c < N:
                dp[row][col] = max(dp[row][col], dp[r][c])
        if dp[row][col] % 3 == milk[row][col]:
            dp[row][col] += 1
print(dp[-1][-1])

"""
import sys
import collections

N = int(sys.stdin.readline())
milk = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# find position of strawberry milk
start = []

que = [(0, 0)]
visited = [[False] * N for _ in range(N)]
visited[0][0] = True
while que:
    new_que = []
    for row, col in que:
        if not milk[row][col]:
            start.append((row, col))
        else:
            for r, c in ((row, col + 1), (row + 1, col)):
                if 0 <= r < N and 0 <= c < N and not visited[r][c]:
                    new_que.append((r, c))
                    visited[r][c] = True
    if start:
        break
    que = new_que

# dynamic programming
dp = [[0] * N for _ in range(N)]
for row, col in start:
    dp[row][col] = 1

que = collections.deque(start)
while que:
    row, col = que.popleft()
    for r, c in ((row, col + 1), (row + 1, col)):
        if 0 <= r < N and 0 <= c < N:
            if not dp[r][c]:
                que.append((r, c))
            dp[r][c] = max(dp[r][c], dp[row][col] + 1 if dp[row][col] % 3 == milk[r][c] else dp[row][col])
print(dp[-1][-1])
"""