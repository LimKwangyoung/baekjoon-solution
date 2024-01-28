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


def bfs(vertex: int) -> None:
    visited[vertex] = True
    que = collections.deque([vertex])
    while que:
        vertex = que.popleft()
        for i in graph[vertex]:
            if not visited[i]:
                visited[i] = True
                que.append(i)


N, M = map(int, sys.stdin.readline().split())

graph = collections.defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = [False] * (N + 1)
for v in range(1, N + 1):
    if not visited[v]:
        if graph[v]:
            dfs(v)
            # bfs(v)
        else:  # a point
            visited[v] = 1
        cnt += 1
print(cnt)
