import sys
import collections


def bfs() -> list:
    result = [None] * (N + 1)

    visited = [False, True] + [False] * (N - 1)
    que = collections.deque([1])
    while que:
        node = que.popleft()
        for i in tree[node]:
            if not visited[i]:
                result[i] = str(node)
                visited[i] = True
                que.append(i)
    return result


N = int(sys.stdin.readline())

tree = collections.defaultdict(list)
for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

print('\n'.join(bfs()[2:]))
