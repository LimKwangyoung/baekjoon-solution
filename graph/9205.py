import sys
import collections


def bfs() -> str:
    def cal_distance(start: int, end: int) -> int:
        x1, y1 = coord[start]
        x2, y2 = coord[end]
        return abs(x1 - x2) + abs(y1 - y2)

    visited = [True] + [False] * (n + 1)

    que = collections.deque([0])
    while que:
        vertex = que.popleft()
        if cal_distance(vertex, n + 1) <= 1000:
            return 'happy'

        for v in range(1, n + 1):
            if not visited[v] and cal_distance(vertex, v) <= 1000:
                que.append(v)
                visited[v] = True
    return 'sad'


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    coord = [tuple(map(int, sys.stdin.readline().split())) for i in range(n + 2)]

    print(bfs())
