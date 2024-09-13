import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())

board = [[False] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = True

result = []
for i in range(M):
    for j in range(N):
        if not board[i][j]:
            area = 1
            que = deque([(i, j)])
            board[i][j] = True
            while que:
                row, col = que.popleft()
                for r, c in ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)):
                    if 0 <= r < M and 0 <= c < N and not board[r][c]:
                        area += 1
                        que.append((r, c))
                        board[r][c] = True
            result.append(area)
print(len(result))
print(*sorted(result))
