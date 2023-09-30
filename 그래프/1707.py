import sys
import collections


def bfs(vertex: int) -> bool:
    visited[vertex] = 0
    que = collections.deque([[vertex, 0]])
    while que:
        vertex, level = que.popleft()
        for i in graph[vertex]:
            if visited[i] is None:
                visited[i] = (level + 1) % 2
                que.append([i, (level + 1) % 2])
            elif visited[i] == level:
                return False
    return True


K = int(sys.stdin.readline())

for _ in range(K):
    graph = collections.defaultdict(list)
    V, E = map(int, sys.stdin.readline().split())
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [None] * (V + 1)
    for v in range(1, V + 1):  # case for unconnected graphs
        if not visited[v] and not bfs(v):
            print('NO')
            break
    else:
        print('YES')
