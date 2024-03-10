import sys
import heapq


def find(node: int) -> int:
    if node == parents[node]:
        return node
    parents[node] = find(parents[node])
    return parents[node]


def union(node_1: int, node_2: int) -> None:
    global result

    root_1 = find(node_1)
    root_2 = find(node_2)
    if root_1 == root_2:
        return

    parents[root_2] = root_1
    result += weight


N, M = map(int, sys.stdin.readline().split())

distances = [list(map(int, sys.stdin.readline().split()))[::-1] for _ in range(M)]
heapq.heapify(distances)

result = 0
parents = [i for i in range(N + 1)]
used = set()
while distances:
    weight, house_1, house_2 = heapq.heappop(distances)
    used.add(house_1)
    used.add(house_2)
    union(house_1, house_2)

    if len(used) == N:
        for i in used:
            find(i)
        if len(set(parents)) == 2:
            result -= weight
            break
print(result)
