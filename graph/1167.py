import sys
import collections


def dfs(start: int) -> tuple[int, int]:
    max_distance, max_vertex = -sys.maxsize, 0

    visited = [False] * (V + 1)
    stack = [(start, 0)]
    while stack:
        vertex, distance = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            if distance > max_distance:
                max_distance = distance
                max_vertex = vertex

            for v, e in tree[vertex]:
                stack.append((v, distance + e))

    return max_vertex, max_distance


V = int(sys.stdin.readline())

tree = collections.defaultdict(list)
for _ in range(V):
    lst = list(map(int, sys.stdin.readline().split()))[:-1]
    for i in range(1, len(lst), 2):
        tree[lst[0]].append([lst[i], lst[i + 1]])  # [vertex, distance]

print(dfs(dfs(1)[0])[1])
