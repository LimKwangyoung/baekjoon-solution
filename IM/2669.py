import sys

board = [[0] * 101 for _ in range(101)]

cnt = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            if not board[i][j]:
                board[i][j] = 1
                cnt += 1
print(cnt)
