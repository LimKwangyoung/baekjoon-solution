import sys


def sequence(lst: list, idx: int) -> None:
    if len(lst) == M:
        print(' '.join(lst))
        return

    for i in range(idx + 1, N + 1):
        sequence(lst + [str(i)], i)


N, M = map(int, sys.stdin.readline().split())

sequence([], 0)
