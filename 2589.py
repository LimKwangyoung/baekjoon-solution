import sys
from collections import deque

height, width = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(height)]

result = float('-inf')
flag = False
for i in range(height):
    if flag:
        break
    for j in range(width):
        if flag:
            break
        if board[i][j] == 'L':
            visited = [[0] * width for _ in range(height)]
            visited[i][j] = 1

            que = deque([(i, j)])
            while que:
                row, col = que.popleft()
                for r, c in ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)):
                    if 0 <= r < height and 0 <= c < width and board[r][c] == 'L' and not visited[r][c]:
                        que.append((r, c))
                        visited[r][c] = visited[row][col] + 1
                        result = max(result, visited[r][c] - 1)

                        if result == width + height - 2:
                            flag = True
                            break
                if flag:
                    break
print(result)
