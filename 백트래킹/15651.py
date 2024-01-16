import sys


def sequence(lst: list) -> None:
    if len(lst) == M:
        print(' '.join(lst))
        return

    for i in range(1, N + 1):
        sequence(lst + [str(i)])


N, M = map(int, sys.stdin.readline().split())

sequence([])
