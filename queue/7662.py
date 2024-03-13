import sys
import heapq
import collections

T = int(sys.stdin.readline())

for _ in range(T):
    max_heap, min_heap = [], []
    nums = collections.defaultdict(int)
    for _ in range(int(sys.stdin.readline())):
        operator, mode = sys.stdin.readline().split()
        mode = int(mode)
        if operator == 'I':
            heapq.heappush(min_heap, mode)
            heapq.heappush(max_heap, -mode)
            nums[mode] += 1
        elif nums:
            if mode == 1:  # maximum
                num = -heapq.heappop(max_heap)
                nums[num] -= 1
                if not nums[num]:
                    del nums[num]
            else:  # minimum
                num = heapq.heappop(min_heap)
                nums[num] -= 1
                if not nums[num]:
                    del nums[num]
        else:
            max_heap, min_heap = [], []

        # print('MAX', max_heap, end='\t')
        # print('MIN', min_heap, end='\t')
        # print(nums)

    print('EMPTY' if not nums else f'{max(nums)} {min(nums)}')
