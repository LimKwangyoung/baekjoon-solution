import sys
import heapq


def find(node: int) -> int:
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]


def union(node_1: int, node_2: int) -> bool:
    root_1 = find(node_1)
    root_2 = find(node_2)
    if root_1 == root_2:
        return False

    if ranks[root_1] < ranks[root_2]:
        parents[root_1] = root_2
    else:
        if ranks[root_1] == ranks[root_2]:
            ranks[root_1] += 1
        parents[root_2] = root_1
    return True


V, E = map(int, sys.stdin.readline().split())

distances = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    heapq.heappush(distances, [C, A, B])

result = 0
cnt = 0

parents = [i for i in range(V + 1)]
ranks = [0 for i in range(V + 1)]
while distances:
    weight, vertex_1, vertex_2 = heapq.heappop(distances)

    ans = union(vertex_1, vertex_2)
    if ans:
        result += weight
        cnt += 1

    if cnt == V - 1:
        break
print(result)
