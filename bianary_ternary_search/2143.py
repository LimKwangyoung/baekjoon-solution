import sys
import collections
import bisect


# Solution 1
def comb_sum(arr: list, length: int) -> dict:
    result_dict = collections.defaultdict(int)
    for i in range(length):
        num = arr[i]
        result_dict[num] += 1
        for j in range(i + 1, length):
            num += arr[j]
            result_dict[num] += 1
    return result_dict


T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A_dict = comb_sum(A, n)
B_dict = comb_sum(B, m)

result = 0
for a in A_dict:
    result += A_dict[a] * B_dict[T - a]
print(result)


# Solution 2
def comb_sum(arr: list, length: int) -> dict:
    result_dict = collections.defaultdict(int)
    for i in range(length):
        num = arr[i]
        result_dict[num] += 1
        for j in range(i + 1, length):
            num += arr[j]
            result_dict[num] += 1
    return result_dict


T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A_dict = comb_sum(A, n)

result = 0
for a_idx in range(m):
    tmp = 0
    for b_idx in range(a_idx, m):
        tmp += B[b_idx]
        result += A_dict[T - tmp]
print(result)


# Solution 3
def comb_sum(arr: list, length: int) -> list:
    result_lst = []
    for i in range(length):
        result_lst.append(arr[i])
        for j in range(i + 1, length):
            result_lst.append(result_lst[-1] + arr[j])
    return result_lst


T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A_lst = comb_sum(A, n)
B_lst = sorted(comb_sum(B, m))

result = 0
for a in A_lst:
    target = T - a

    left = bisect.bisect_left(B_lst, target)
    right = bisect.bisect_right(B_lst, target)
    result += (right - left)

    # left, right = 0, len(B_lst)
    # while left <= right:
    #     mid = (left + right) // 2
    #     if B_lst[mid] >= target:
    #         right = mid - 1
    #     else:
    #         left = mid + 1
    # final_left = left
    #
    # left, right = 0, len(B_lst)
    # while left <= right:
    #     mid = (left + right) // 2
    #     if B_lst[mid] <= target:
    #         left = mid + 1
    #     else:
    #         right = mid - 1
    # final_right = left
    #
    # result += (final_right - final_left)

print(result)
