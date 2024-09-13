import sys
from collections import defaultdict


def find(vertex: int) -> int:
    if roots[vertex] == vertex:
        return vertex
    roots[vertex] = find(roots[vertex])
    return roots[vertex]


N, M, k = map(int, sys.stdin.readline().split())
payments = [0] + list(map(int, sys.stdin.readline().split()))

roots = list(range(N + 1))
for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())

    root_1 = find(v)
    root_2 = find(w)

    if root_1 == root_2:
        break
    roots[root_1] = root_2

result = defaultdict(lambda: float('inf'))
for i in range(1, N + 1):
    find(i)
    result[roots[i]] = min(result[roots[i]], payments[i], payments[roots[i]])

total = sum(i for i in result.values())
print(total if total <= k else 'Oh no')
