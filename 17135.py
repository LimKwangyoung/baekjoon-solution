import sys
import collections
import heapq

N, M, D = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().split() for _ in range(N)]

idx = 0
enemies = dict()
for i in range(M):
    for j in range(N):
        if board[j][i] == '1':
            enemies[idx] = (j, i)
            idx += 1

archers = {i: (N, i) for i in range(M)}

distances = collections.defaultdict(list)
for archer, (x1, y1) in archers.items():
    for enemy, (x2, y2) in enemies.items():
        heapq.heappush(distances[archer], (abs(x1 - x2) + abs(y1 - y2), enemy))  # (distance, enemy)

while enemies:
    # print(enemies.keys())
    print(distances)
    minimum = min(distances[archer][0][0] for archer in range(M))
    print(minimum)
    for archer in range(M):
        while distances[archer][0][1] not in enemies.keys():
            heapq.heappop(distances[archer])

        if distances[archer][0][0] <= minimum + D:
            _, enemy = heapq.heappop(distances[archer])
            if enemy in enemies:
                del enemies[enemy]
    print(distances)
    print()
