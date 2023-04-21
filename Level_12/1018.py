import sys


def count_painting(lst: list, row: int, col: int) -> int:
    # cnt_1 is the case of starting 'B', and cnt_2 is the case of starting 'W'.
    cnt_1, cnt_2 = 0, 0
    for row_idx in range(8):
        for col_idx in range(8):
            if (row_idx + col_idx) % 2 == 0:
                if lst[row + row_idx][col + col_idx] == 'W':
                    cnt_1 += 1
                else:
                    cnt_2 += 1
            else:
                if lst[row + row_idx][col + col_idx] == 'B':
                    cnt_1 += 1
                else:
                    cnt_2 += 1

    return min(cnt_1, cnt_2)


N, M = map(int, input().split())
chess_lst = sys.stdin.readlines()

minimum = 64
for i in range(N - 7):
    for j in range(M - 7):
        painting_cnt = count_painting(chess_lst, i, j)
        if painting_cnt < minimum:
            minimum = painting_cnt
print(minimum)
