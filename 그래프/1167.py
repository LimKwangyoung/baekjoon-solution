import sys
import collections


def bfs(start: int) -> int:
    result = [0] * (V + 1)
    que = collections.deque([start])
    while que:
        row = que.popleft()
        for vertex, distance in tree[row]:
            if vertex != start and not result[vertex]:
                result[vertex] = result[row] + distance
                que.append(vertex)
    return max(result)


V = int(sys.stdin.readline())

tree = collections.defaultdict(list)
leaf = []
for _ in range(V):
    lst = list(map(int, sys.stdin.readline().split()))[:-1]
    for i in range(1, len(lst), 2):
        tree[lst[0]].append([lst[i], lst[i + 1]])
    if i == 1:
        leaf.append(lst[0])


