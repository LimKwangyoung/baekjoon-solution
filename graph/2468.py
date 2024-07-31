import sys
import collections


def bfs(rain_height: int) -> int:
    total = 0

    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > rain_height and not visited[i][j]:
                visited[i][j] = True
                total += 1

                que = collections.deque([(i, j)])
                while que:
                    row, col = que.popleft()

                    for r, c in ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)):
                        if 0 <= r < N and 0 <= c < N and board[r][c] > rain_height and not visited[r][c]:
                            visited[r][c] = True
                            que.append((r, c))
    return total


N = int(sys.stdin.readline())

minimum, maximum = float('inf'), float('-inf')
board = []
for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    minimum = min(minimum, min(lst))
    maximum = max(maximum, max(lst))
    board.append(lst)

if minimum == maximum:
    print(1)
else:
    print(max(bfs(height) for height in range(minimum, maximum)))
