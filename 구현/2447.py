import sys


# Solution 1
def star(row: int, col: int, idx: int) -> None:
    if idx == 1:
        board[row][col] = '*'
        return

    for r in range(row, row + idx, idx // 3):
        for c in range(col, col + idx, idx // 3):
            if (r, c) == (row + idx // 3, col + idx // 3):
                continue
            star(r, c, idx // 3)


N = int(sys.stdin.readline())

board = [[' '] * N for _ in range(N)]
star(0, 0, N)

for i in board:
    print(''.join(i))


# Solution 2 (faster than Solution 1)
def star(n: int) -> list:
    if n == 1:
        return ['*']

    result = []

    prev = star(n // 3)
    for i in prev:
        result.append(i * 3)
    for i in prev:
        result.append(i + ' ' * (n // 3) + i)
    for i in prev:
        result.append(i * 3)

    return result


N = int(sys.stdin.readline())
print('\n'.join(star(N)))
