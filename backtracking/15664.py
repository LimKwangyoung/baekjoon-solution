import sys


def sequence(lst: list, idx: int) -> None:
    if len(lst) == M and ' '.join(lst) not in visited:
        print(' '.join(lst))
        visited.add(' '.join(lst))
        return

    for i in range(idx, N):
        sequence(lst + [str(nums[i])], i + 1)


N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

visited = set()
sequence([], 0)
