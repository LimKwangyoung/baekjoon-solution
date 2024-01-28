import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    graph = [0] + list(map(int, sys.stdin.readline().split()))

    cnt = 0
    visited = [False] * (N + 1)
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            vertex = graph[i]
            while not visited[vertex]:
                visited[vertex] = True
                vertex = graph[vertex]
            cnt += 1
    print(cnt)
