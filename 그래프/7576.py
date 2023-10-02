import sys
import collections

M, N = map(int, sys.stdin.readline().split())

no_tomato = 0
grid = []
que = collections.deque()
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    no_tomato += lst.count(-1)
    grid.append(lst[:])
    while 1 in lst:
        idx = lst.index(1)
        que.append((i, idx, 0))
        lst[idx] = 0

while que:
    row, col, day = que.popleft()
    coordinate = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
    for r, c in coordinate:
        if 0 <= r < N and 0 <= c < M and not grid[r][c]:
            grid[r][c] = 1
            que.append((r, c, day + 1))
print(day)
