import sys

N, M = map(int, sys.stdin.readline().split())

board = [[0] * M for _ in range(N)]
total = 0
rows, cols = [0] * N, [0] * M
for i in range(N):
    nums = int(sys.stdin.readline())
    for j in range(M):
        nums, num = divmod(nums, 10)
        board[i][M - 1 - j] = num
        total += num
        rows[i] += num
        cols[M - 1 - j] += num

result = -sys.maxsize

area_1 = area_11 = 0
for i in range(N - 1):
    area_1 += rows[i]
    area_11 += rows[N - 1 - i]

    # 3 horizons
    area_2 = 0
    for j in range(i + 1, N - 1):
        area_2 += rows[j]
        area_3 = total - (area_1 + area_2)
        result = max(result, area_1 * area_2 * area_3)

    # 1 horizon and 2 verticals
    area_2 = area_22 = 0
    for j in range(M - 1):
        area_2 += sum(board[row][j] for row in range(i + 1, N))
        area_22 += sum(board[row][j] for row in range(N - 1 - i))
        area_3 = total - (area_1 + area_2)
        area_33 = total - (area_11 + area_22)
        result = max(result, area_1 * area_2 * area_3)
        result = max(result, area_11 * area_22 * area_33)

area_1 = area_11 = 0
for i in range(M - 1):
    area_1 += cols[i]
    area_11 += cols[M - 1 - i]

    # 3 verticals
    area_2 = 0
    for j in range(i + 1, M - 1):
        area_2 += cols[j]
        area_3 = total - (area_1 + area_2)
        result = max(result, area_1 * area_2 * area_3)

        # 1 vertical and 2 horizons
    area_2 = area_22 = 0
    for j in range(N - 1):
        area_2 += sum(board[j][col] for col in range(i + 1, M))
        area_22 += sum(board[j][col] for col in range(M - 1 - i))
        area_3 = total - (area_1 + area_2)
        area_33 = total - (area_11 + area_22)
        result = max(result, area_1 * area_2 * area_3)
        result = max(result, area_11 * area_22 * area_33)
print(result)
