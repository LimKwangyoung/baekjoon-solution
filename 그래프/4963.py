import sys


def dfs(row: int, col: int) -> None:
    stack = [(row, col)]
    while stack:
        row, col = stack.pop()
        if grid[row][col]:
            grid[row][col] = 0
            coordinate = [(row - 1, col), (row - 1, col + 1), (row, col + 1), (row + 1, col + 1),
                          (row + 1, col), (row + 1, col - 1), (row, col - 1), (row - 1, col - 1)]
            for r, c in coordinate:
                if 0 <= r < h and 0 <= c < w and grid[r][c]:
                    stack.append((r, c))


while True:
    w, h = map(int, sys.stdin.readline().split())
    if (w, h) == (0, 0):
        break

    grid = []
    for _ in range(h):
        grid.append(list(map(int, sys.stdin.readline().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)
