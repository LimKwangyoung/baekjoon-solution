import sys
import heapq

N, M, K = map(int, sys.stdin.readline().split())
beers = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(K)], key=lambda x: (x[1], x[0]))

total = cnt = 0
que = []
for preference, level in beers:
    heapq.heappush(que, preference)
    total += preference
    cnt += 1
    if cnt == N:
        if total >= M:
            print(level)
            break
        else:
            minimum = heapq.heappop(que)
            total -= minimum
            cnt -= 1
else:
    print(-1)
