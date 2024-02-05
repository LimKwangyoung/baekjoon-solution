import sys


# Solution 1
def dfs(city: str) -> None:
    stack = [city]
    while stack:
        city = stack.pop()
        if city not in visited:
            visited.add(city)
            for i in range(N):
                if graph[city][i] == '1':
                    stack.append(i)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [sys.stdin.readline().split() for _ in range(N)]
cities = list(map(lambda x: x - 1, map(int, sys.stdin.readline().split())))

visited = set()
dfs(cities[0])

print('YES' if set(cities).issubset(visited) else 'NO')


# Solution 2
def find_root(node: int) -> int:
    if parents[node] == node:
        return node

    parents[node] = find_root(parents[node])
    return parents[node]


def union(node_1: int, node_2: int) -> None:
    root_1 = find_root(node_1)
    root_2 = find_root(node_2)

    if root_1 == root_2:
        return
    # low level must be contained in high level
    if level[root_1] < level[root_2]:
        parents[root_1] = root_2
    else:
        parents[root_2] = root_1
        # if level of root_1 and root_2 are the same
        if level[root_1] == level[root_2]:
            level[root_1] += 1


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parents = [i for i in range(N)]
level = [0] * N
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(i + 1, N):
        if lst[j]:
            union(i, j)

plans = list(map(int, sys.stdin.readline().split()))
root_city = find_root(plans[0] - 1)
for i in plans[1:]:
    if root_city != find_root(parents[i - 1]):
        print('NO')
        break
else:
    print('YES')
