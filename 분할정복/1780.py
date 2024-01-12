import sys
import collections


def main(row: int, col: int, idx: int):
    num = board[row][col]
    for r in range(row, row + idx):
        for c in range(col, col + idx):
            if board[r][c] != num:
                for i in range(row, row + idx, idx // 3):
                    for j in range(col, col + idx, idx // 3):
                        main(i, j, idx // 3)
                return
    cnt[num] += 1
    return


N = int(sys.stdin.readline())
board = [sys.stdin.readline().split() for _ in range(N)]

cnt = collections.defaultdict(int)
main(0, 0, N)

print(cnt['-1'])
print(cnt['0'])
print(cnt['1'])
