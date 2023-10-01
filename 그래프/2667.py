import sys


def dfs(row: int, col: int) -> int:
    cnt = 0
    stack = [(row, col)]
    while stack:
        row, col = stack.pop()
        if grid[row][col]:
            grid[row][col] = 0
            cnt += 1
            coordinate = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
            for r, c in coordinate:
                if 0 <= r < N and 0 <= c < N and grid[r][c]:
                    stack.append((r, c))
    return cnt


N = int(sys.stdin.readline())

grid = []
for _ in range(N):
    grid.append([int(i) for i in sys.stdin.readline().rstrip()])

result = []
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            result.append(dfs(i, j))

result.sort()
print(len(result))
print('\n'.join(map(str, result)))
