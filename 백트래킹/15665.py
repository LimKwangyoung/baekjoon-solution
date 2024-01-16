import sys


def sequence(lst: list) -> None:
    if len(lst) == M:
        if ' '.join(lst) not in visited:
            print(' '.join(lst))
            visited.add(' '.join(lst))
        return

    for i in nums:
        sequence(lst + [str(i)])


N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

visited = set()
sequence([])
