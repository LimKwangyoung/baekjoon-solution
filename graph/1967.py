import sys
import collections


def dfs(start: int) -> tuple[int, int]:
    max_distance, max_vertex = -sys.maxsize, 0

    visited = [False] * (n + 1)
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


n = int(sys.stdin.readline())

tree = collections.defaultdict(list)
for lst in sys.stdin.readlines():
    parent, child, weight = map(int, lst.split())
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])

print(dfs(dfs(1)[0])[1])
