import sys
import collections
import heapq

N, K = sys.stdin.readline().split()
N_lst = list(map(int, list(N)))
K = int(K)

if len(N_lst) == 1 or (len(N_lst) == 2 and sum(N_lst[1:]) == 0):
    print(-1)
else:
    nums = []
    indices = collections.defaultdict(list)
    for i, val in enumerate(N_lst):
        heapq.heappush(nums, -val)
        heapq.heappush(indices[val], -i)

    # print(f'NUMS: {nums}')
    # print(f'INDICES: {indices}')
    # print(f'N_lst: {N_lst}')
    # print()

    idx1 = 0
    while idx1 < len(N_lst) and K:
        if N_lst[idx1] < -nums[0]:
            # select maximum
            num1, num2 = N_lst[idx1], -heapq.heappop(nums)
            # select index of maximum
            idx2 = -heapq.heappop(indices[num2])
            # exchange
            N_lst[idx1], N_lst[idx2] = N_lst[idx2], N_lst[idx1]
            # update indices
            tmp = [-idx2]
            while indices[num1] and indices[num1][0] != -idx1:
                heapq.heappush(tmp, -heapq.heappop(indices[num1]))
            if indices[num1]:
                heapq.heappop(indices[num1])
            while indices[num1]:
                heapq.heappush(tmp, -heapq.heappop(indices[num1]))
            indices[num1] = tmp
            heapq.heappush(indices[num2], -idx1)

            K -= 1
            idx1 += 1
            # heapq.heappop(nums)

            # print(f'NUMS: {nums}')
            # print(f'INDICES: {indices}')
            # print(f'N_lst: {N_lst}')
            # print(f'INDEX: {idx1}')
            # print()
        else:
            break
    # print(f'K: {K}')
    if K % 2:
        N_lst[-1], N_lst[-2] = N_lst[-2], N_lst[-1]
    print(''.join(map(str, N_lst)))