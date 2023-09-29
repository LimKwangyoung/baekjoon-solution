import sys
import collections


def dfs_recursion(start: int) -> list:
    def dfs(vertex: int, lst: list):
        lst.append(vertex)
        visited[vertex] = True
        for v in graph[vertex]:
            if not visited[v]:
                dfs(v, lst)
        return lst

    visited = [False] * (N + 1)
    return dfs(start, [])


def dfs_stack(start: int) -> list:
    for v in graph:
        graph[v].sort(reverse=True)

    result = []
    visited = [False] * (N + 1)
    stack = [start]
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            result.append(vertex)
            visited[vertex] = True
            for v in graph[vertex]:
                stack.append(v)
    return result


def bfs(start: int) -> list:
    result = [start]
    visited = [False] * (N + 1)
    visited[start] = True
    que = collections.deque([start])
    while que:
        vertex = que.popleft()
        for v in graph[vertex]:
            if not visited[v]:
                result.append(v)
                visited[v] = True
                que.append(v)
    return result


N, M, V = map(int, sys.stdin.readline().split())

graph = collections.defaultdict(list)
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for i in graph:
    graph[i].sort()

print(*dfs_recursion(V))
# print(*dfs_stack(V))
print(*bfs(V))
