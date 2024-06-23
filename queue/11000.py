import sys
import heapq

N = int(sys.stdin.readline())
classes = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

que = [classes[0][1]]
for start, end in classes[1:]:
    # continue class
    if que[0] <= start:
        heapq.heappop(que)
        heapq.heappush(que, end)
    # open new class
    else:
        heapq.heappush(que, end)
print(len(que))
