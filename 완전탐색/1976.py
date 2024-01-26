import sys


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
