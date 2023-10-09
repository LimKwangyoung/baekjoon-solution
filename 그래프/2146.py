import sys
import collections


def number_island(row: int, col: int) -> None:
    grid[row][col] = str(island)
    que = collections.deque([(row, col)])
    while que:
        row, col = que.popleft()
        coordinate = [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]
        for r, c in coordinate:
            if 0 <= r < N and 0 <= c < N:
                if grid[r][c] == 1:  # island
                    grid[r][c] = str(island)
                    que.append((r, c))
                elif grid[r][c] == 0:  # shore
                    shores[str(island)].add((row, col))


def find_distance(idx: int) -> int:
    visited = [[0] * N for _ in range(N)]

    que = collections.deque(list(shores[str(idx)]))
    while que:
        row, col = que.popleft()
        coordinate = [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]
        for r, c in coordinate:
            if 0 <= r < N and 0 <= c < N and int(grid[r][c]) != idx and not visited[r][c]:
                if grid[r][c] == 0:  # sea
                    visited[r][c] = visited[row][col] + 1
                    que.append((r, c))
                elif int(grid[r][c]) > idx:  # arrive at another island for the first time
                    return visited[row][col]


N = int(sys.stdin.readline())

grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

# number islands and get coordinates of shores
island = 1
shores = collections.defaultdict(set)
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            number_island(i, j)
            island += 1

# find the shortest distance
length = sys.maxsize
for i in range(1, len(shores)):
    length = min(length, find_distance(i))
    if length == 1:  # speedup condition
        break
print(length)
