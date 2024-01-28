import sys


def sequence(lst: list, idx: set) -> None:
    if len(lst) == M:
        statement = ' '.join(lst)
        if statement not in visited:
            visited.add(statement)
            print(' '.join(lst))
            return

    for i in range(N):
        if i not in idx:
            idx.add(i)
            sequence(lst + [str(nums[i])], idx)
            idx.remove(i)


N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

visited = set()
sequence([], set())
