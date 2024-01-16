import sys


def sequence(lst: list) -> None:
    if len(lst) == M:
        print(' '.join(map(str, lst)))
        return

    for i in range(1, N + 1):
        if i not in set(lst):
            sequence(lst + [i])


N, M = map(int, sys.stdin.readline().split())

sequence([])
