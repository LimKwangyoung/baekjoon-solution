import sys
import heapq
import collections

T = int(sys.stdin.readline())

for _ in range(T):
    max_heap, min_heap = [], []
    nums = collections.defaultdict(int)

    cnt = 0
    for _ in range(int(sys.stdin.readline())):
        operator, mode = sys.stdin.readline().split()
        mode = int(mode)
        if operator == 'I':
            heapq.heappush(min_heap, mode)
            heapq.heappush(max_heap, -mode)
            nums[mode] += 1
            cnt += 1
        elif cnt:
            if mode == 1:  # maximum
                while True:
                    num = -heapq.heappop(max_heap)
                    if nums[num]:
                        nums[num] -= 1
                        break
            else:  # minimum
                while True:
                    num = heapq.heappop(min_heap)
                    if nums[num]:
                        nums[num] -= 1
                        break
            cnt -= 1

    nums = [num for num in nums if nums[num]]
    print('EMPTY' if not nums else f'{max(nums)} {min(nums)}')
