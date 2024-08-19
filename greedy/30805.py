import sys
import collections


def common_sequence(idx_1: int, idx_2: int) -> list:
    A_index = collections.defaultdict(list)
    B_index = collections.defaultdict(list)

    for idx in range(idx_1, N):
        A_index[A[idx]].append(idx)

    for idx in range(idx_2, M):
        B_index[B[idx]].append(idx)

    for num in sorted(A_index, reverse=True):
        if num in B_index:
            return [num] + common_sequence(A_index[num][0] + 1, B_index[num][0] + 1)
    return []


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

result = common_sequence(0, 0)
print(len(result))
if len(result) > 0:
    print(*result)
