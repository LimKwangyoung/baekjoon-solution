N = int(input())
matrix = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            matrix[x + i][y + j] = 1

result = 0
for i in matrix:
    result += sum(i)
print(result)