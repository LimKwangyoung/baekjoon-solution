import sys
import collections

# Solution 1(DFS)
N, M = map(int, sys.stdin.readline().split())

grid = []
for _ in range(N):
    grid.append([int(i) for i in sys.stdin.readline().rstrip()])
cnt_lst = [[M * N for _ in range(M)] for _ in range(N)]

stack = [(0, 0, 1)]
while stack:
    row, col, cnt = stack.pop()
    if cnt < cnt_lst[row][col]:
        cnt_lst[row][col] = cnt
        coordinate = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
        for i, j in coordinate:
            if 0 <= i < N and 0 <= j < M and grid[i][j]:
                stack.append((i, j, cnt + 1))
print(cnt_lst[N - 1][M - 1])

# Solution 2(BFS)
N, M = map(int, sys.stdin.readline().split())

grid = []
for _ in range(N):
    grid.append([int(i) for i in sys.stdin.readline().rstrip()])

visited = [[False] * M for _ in range(N)]
visited[0][0] = True
que = collections.deque([(0, 0)])  # faster than Solution 1
while que:
    row, col = que.popleft()
    coordinate = [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]
    for i, j in coordinate:
        if 0 <= i < N and 0 <= j < M and grid[i][j] > 0 and not visited[i][j]:
            que.append((i, j))
            grid[i][j] = grid[row][col] + 1
            visited[i][j] = True
print(grid[N - 1][M - 1])
