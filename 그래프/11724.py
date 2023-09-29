import sys
import collections


def dfs(vertex: int) -> None:
    stack = [vertex]
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            for i in graph[vertex]:
                stack.append(i)


N, M = map(int, sys.stdin.readline().split())

graph = collections.defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = [False] * (N + 1)
for v in graph:
    if not visited[v]:
        cnt += 1
        dfs(v)
print(cnt)
