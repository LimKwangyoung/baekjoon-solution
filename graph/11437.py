import sys
import collections


def lca(node_1: int, node_2: int) -> int:
    if ranks[node_1] > ranks[node_2]:
        node_1, node_2 = node_2, node_1

    if (node_1, node_2) in check:
        return check[(node_1, node_2)]

    tmp = [(node_1, node_2)]

    while ranks[node_1] != ranks[node_2]:
        node_2 = parents[node_2]

        if (node_1, node_2) in check:
            for x, y in tmp:
                check[(x, y)] = check[(node_1, node_2)]
            return check[(node_1, node_2)]

        tmp.append((node_1, node_2))

    while node_1 != node_2:
        node_1 = parents[node_1]
        node_2 = parents[node_2]
        tmp.append((node_1, node_2))
    result = node_1

    for x, y in tmp:
        check[(x, y)] = result
    return result


N = int(sys.stdin.readline())

graph = collections.defaultdict(list)
for _ in range(N - 1):
    vertex_1, vertex_2 = map(int, sys.stdin.readline().split())
    graph[vertex_1].append(vertex_2)
    graph[vertex_2].append(vertex_1)

# make a tree
parents = list(range(N + 1))
ranks = [0] * (N + 1)
que = collections.deque([1])
while que:
    vertex = que.popleft()
    for v in graph[vertex]:
        if v != 1 and parents[v] == v:
            parents[v] = vertex
            ranks[v] = ranks[vertex] + 1
            que.append(v)

# Least Common Ancestor
M = int(sys.stdin.readline())

# dictionary for saving path
check = dict()
for _ in range(M):
    vertex_1, vertex_2 = map(int, sys.stdin.readline().split())
    print(lca(vertex_1, vertex_2))
