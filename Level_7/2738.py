N, M = map(int, input().split())

result = []
for _ in range(N):
    result.append([0] * M)
for _ in range(2):
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(M):
            result[i][j] += line[j]

for i in result:
    for j in i:
        print(j, end=' ')
    print()