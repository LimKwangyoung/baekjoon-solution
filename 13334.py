import sys
import heapq

n = int(sys.stdin.readline())
nums = [sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
d = int(sys.stdin.readline())

positions = dict()
lst = []  # (position, start or end, number)
for i in range(n):
    positions[i] = nums[i]
    heapq.heappush(lst, (nums[i][0], i))

result = 0
while lst:
    position, number = heapq.heappop(lst)

    tmp = 0
    for x, y in positions.values():
        if position <= x and y <= position + d:
            tmp += 1
    result = max(result, tmp)

    del positions[number]
print(result)
