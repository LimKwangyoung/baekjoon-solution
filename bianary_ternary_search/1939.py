import sys
from collections import deque


def bfs(weight: int) -> bool:
    que = deque([src])
    visited = [False] * (N + 1)
    visited[src] = True

    while que:
        vertex = que.popleft()

        for v, w in bridges[vertex]:
            if not visited[v] and w >= weight:
                visited[v] = True
                que.append(v)

    if visited[dst]:
        return True
    else:
        return False


N, M = map(int, sys.stdin.readline().split())
bridges = [[] for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    bridges[a].append([b, c])
    bridges[b].append([a, c])

src, dst = map(int, sys.stdin.readline().split())

start, end = 1, 1000000000

result = 0
while start <= end:
    mid = (start + end) // 2

    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
