import sys
import collections


def check_island(row: int, col: int) -> None:
    grid[row][col] = str(island)
    que = collections.deque([(row, col)])
    while que:
        row, col = que.popleft()
        coordinate = [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]
        for r, c in coordinate:
            if 0 <= r < N and 0 <= c < N and grid[r][c] == 1:
                grid[r][c] = str(island)
                que.append((r, c))


def find_distance(row: int, col: int, start: int) -> int:
    result = sys.maxsize
    cnt_lst = [[False] * N for _ in range(N)]
    cnt_lst[row][col] = 0
    que = collections.deque([(row, col)])
    while que:
        row, col = que.popleft()
        coordinate = [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]
        for r, c in coordinate:
            if 0 <= r < N and 0 <= c < N and cnt_lst[r][c] is False:
                if grid[r][c] == 0:
                    cnt_lst[r][c] = cnt_lst[row][col] + 1
                    que.append((r, c))
                elif grid[r][c] == str(start):  # same island
                    cnt_lst[r][c] = 0
                    que.append((r, c))
                else:  # another island
                    result = min(result, cnt_lst[row][col])
    return result


N = int(sys.stdin.readline())

grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

# number islands
island = 1
island_lst = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            check_island(i, j)
            island_lst.append((i, j))
            island += 1

# find the shortest distance
length = sys.maxsize
for num in range(len(island_lst) - 1):
    i, j = island_lst[num]
    length = min(length, find_distance(i, j, num + 1))
print(length)
