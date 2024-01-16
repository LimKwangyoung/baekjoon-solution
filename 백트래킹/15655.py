import sys


def sequence(lst: list, idx: int) -> None:
    if len(lst) == M:
        print(' '.join(lst))
        return

    for i in range(idx, N):
        sequence(lst + [str(nums[i])], i + 1)


N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

sequence([], 0)
