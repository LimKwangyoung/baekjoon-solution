import sys


def comb_sum(arr: list, length: int) -> list:
    result = []
    for i in range(length):
        result.append(arr[i])
        for j in range(i + 1, length):
            result.append(result[-1] + arr[j])
    return result


T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A_lst = comb_sum(A, n)
B_lst = comb_sum(B, m)

nums_lst = []
for a in A_lst:


left, right = A_lst[0] + B_lst[0], A_lst[-1] + B_lst[-1]