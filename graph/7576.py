import sys
import collections

M, N = map(int, sys.stdin.readline().split())

tomato, no_tomato = 0, 0
grid = []
que = collections.deque()
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    grid.append(lst)
    for j in range(M):
        if lst[j] == 1:
            que.append((i, j, 0))
            tomato += 1
        elif lst[j] == -1:
            no_tomato += 1

while que:
    row, col, day = que.popleft()
    coordinate = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
    for r, c in coordinate:
        if 0 <= r < N and 0 <= c < M and not grid[r][c]:
            grid[r][c] = 1
            que.append((r, c, day + 1))
            tomato += 1
print(day if tomato + no_tomato == M * N else -1)
