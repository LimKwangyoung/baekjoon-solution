import sys
import collections
import heapq
from itertools import combinations
from copy import deepcopy


def attack(enemies: dict, distances: dict, candidates: list) -> int:
    total = time = 0
    while enemies:
        tmp = []
        for archer in candidates:
            while distances[archer][0][1] not in enemies.keys():
                heapq.heappop(distances[archer])

            if distances[archer][0][0] - time <= D:
                _, enemy = heapq.heappop(distances[archer])
                tmp.append(enemy)

        for enemy in tmp:
            if enemy in enemies:
                del enemies[enemy]
                total += 1

            if not enemies:
                return total

        time += 1
        for enemy, (x, y) in list(enemies.items()):
            if (N - x) <= time:
                del enemies[enemy]
    return total


N, M, D = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().split() for _ in range(N)]

# dictionary of enemies' positions
idx = 0
enemies_dict = dict()
for j in range(M):
    for i in range(N):
        if board[i][j] == '1':
            enemies_dict[idx] = (i, j)
            idx += 1

# dictionary of archers' positions
archers = {i: (N, i) for i in range(M)}

# dictionary of distances for each archer
distances_dict = collections.defaultdict(list)
for a, (x1, y1) in archers.items():
    for e, (x2, y2) in enemies_dict.items():
        heapq.heappush(distances_dict[a], (abs(x1 - x2) + abs(y1 - y2), e))  # (distance, enemy)

result = float('-inf')
for archer_lst in combinations(list(range(M)), 3):
    result = max(result, attack(deepcopy(enemies_dict), deepcopy(distances_dict.copy()), archer_lst))
print(result)
