import sys
import collections
import math


def lca(node_1: int, node_2: int) -> int:
    if ranks[node_1] > ranks[node_2]:
        node_1, node_2 = node_2, node_1

    for l in range(LOG - 1, -1, -1):
        if ranks[node_2] - ranks[node_1] >= 2**l:
            node_2 = parents[node_2][l]

    if node_1 == node_2:
        return node_1

    for l in range(LOG - 1, -1, -1):
        if parents[node_1][l] != parents[node_2][l]:
            node_1 = parents[node_1][l]
            node_2 = parents[node_2][l]
    return parents[node_1][0]


N = int(sys.stdin.readline())

graph = collections.defaultdict(list)
for _ in range(N - 1):
    vertex_1, vertex_2 = map(int, sys.stdin.readline().split())
    graph[vertex_1].append(vertex_2)
    graph[vertex_2].append(vertex_1)

LOG = math.ceil(math.log2(N + 1))
parents = [[i] + [0 for _ in range(LOG - 1)] for i in range(N + 1)]
ranks = [0] * (N + 1)
que = collections.deque([1])
while que:
    vertex = que.popleft()
    for v in graph[vertex]:
        if v != 1 and parents[v][0] == v:
            parents[v][0] = vertex
            ranks[v] = ranks[vertex] + 1
            que.append(v)

for i in range(1, LOG):
    for j in range(1, N + 1):
        parents[j][i] = parents[parents[j][i - 1]][i - 1]

M = int(sys.stdin.readline())
for _ in range(M):
    vertex_1, vertex_2 = map(int, sys.stdin.readline().split())
    print(lca(vertex_1, vertex_2))