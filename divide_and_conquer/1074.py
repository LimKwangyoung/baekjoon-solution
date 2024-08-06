import sys


def zigzag(length: int, row: int, col: int) -> int:
    if not length:
        return 0

    if row < 2**(length - 1):
        if col < 2**(length - 1):
            quarter = 1
        else:
            quarter = 2
            col -= 2**(length - 1)
    else:
        if col < 2**(length - 1):
            quarter = 3
            row -= 2**(length - 1)
        else:
            quarter = 4
            row -= 2**(length - 1)
            col -= 2**(length - 1)
    return 2**(2 * length) * (quarter - 1) // 4 + zigzag(length - 1, row, col)


N, r, c = map(int, sys.stdin.readline().split())

print(zigzag(N, r, c))
