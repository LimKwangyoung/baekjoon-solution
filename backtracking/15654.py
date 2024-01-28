import sys


def sequence(lst: list) -> None:
    if len(lst) == M:
        print(' '.join(lst))
        return

    for i in range(N):
        if str(nums[i]) not in set(lst):
            sequence(lst + [str(nums[i])])


N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

sequence([])
