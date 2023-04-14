matrix = [list(map(int, input().split())) for _ in range(9)]

max_row, max_col, maximum = 0, 0, -1 # 모든 행렬값이 0일 경우도 고려
for i in range(9):
    for j in range(9):
        if matrix[i][j] > maximum:
            max_row, max_col = i + 1, j + 1
            maximum = matrix[i][j]
print(maximum)
print(max_row, max_col)