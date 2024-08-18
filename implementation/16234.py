import sys
import collections


def bfs(row: int, col: int) -> int:
    total = board[row][col]
    result = [(row, col)]

    que = collections.deque([(row, col)])
    while que:
        row, col = que.popleft()
        for r, c in ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)):
            if 0 <= r < N and 0 <= c < N and not visited[r][c] and L <= abs(board[row][col] - board[r][c]) <= R:
                visited[r][c] = True
                que.append((r, c))
                total += board[r][c]
                result.append((r, c))

    for r, c in result:
        board[r][c] = total // len(result)

    return len(result)


N, L, R = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0
flag = 0
while flag != 1:
    flag = 0

    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                flag = max(flag, bfs(i, j))
    cnt += 1
print(cnt - 1)
