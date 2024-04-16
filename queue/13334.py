import sys
import heapq

n = int(sys.stdin.readline())
nums = sorted([sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(n)], key=lambda x: x[1])
d = int(sys.stdin.readline())

result = 0
candidates = []
for start, end in nums:
    heapq.heappush(candidates, start)
    while candidates and candidates[0] + d < end:
        heapq.heappop(candidates)
    result = max(result, len(candidates))
print(result)
