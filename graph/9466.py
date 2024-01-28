import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    student = [0] + list(map(int, sys.stdin.readline().split()))

    cnt = 0
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            lst = [i]
            visited[i] = True
            vertex = student[i]
            while not visited[vertex]:
                lst.append(vertex)
                visited[vertex] = True
                vertex = student[vertex]

            if vertex in lst:
                cnt += len(lst) - lst.index(vertex)
    print(n - cnt)
