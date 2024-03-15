import sys


def find(node: int) -> int:
    if node == parents[node]:
        return parents[node]
    parents[node] = find(parents[node])
    return parents[node]


def union(node_1: int, node_2: int) -> bool:
    root_1 = find(node_1)
    root_2 = find(node_2)
    if root_1 == root_2:
        return True
    parents[root_1] = root_2
    return False


sys.setrecursionlimit(999999999)
n, m = map(int, sys.stdin.readline().split())

result = 0
parents = [i for i in range(n)]
for num in range(1, m + 1):
    vertex_1, vertex_2 = map(int, sys.stdin.readline().split())
    ans = union(vertex_1, vertex_2)
    if ans:
        result = num
        for _ in range(m - num):
            sys.stdin.readline()
        break
print(result)
