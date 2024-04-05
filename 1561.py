import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))

if N <= M:
    print(N)
else:
    rides = [(time, i) for i, time in enumerate(times)]
    heapq.heapify(rides)
    for i in range(M, N):
        min_time, min_idx = heapq.heappop(rides)
        heapq.heappush(rides, (min_time + times[min_idx], min_idx))
        # min_idx, min_time = 0, float('inf')
        # for idx, time in enumerate(rides):
        #     if time < min_time:
        #         min_idx = idx
        #         min_time = time
        # rides[min_idx] += times[min_idx]
    print(min_idx + 1)