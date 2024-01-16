import sys


def quad_tree(row: int, col: int, idx: int) -> str:
    if idx == 1:
        return images[row][col]

    idx //= 2
    lst = [quad_tree(row, col, idx), quad_tree(row, col + idx, idx),
           quad_tree(row + idx, col, idx), quad_tree(row + idx, col + idx, idx)]
    if len(set(lst)) == 1 and lst[0] in ('0', '1'):
        return lst[0]
    return f'({"".join(lst)})'


N = int(sys.stdin.readline())

images = [list(sys.stdin.readline()[:-1]) for _ in range(N)]
print(quad_tree(row=0, col=0, idx=N))
