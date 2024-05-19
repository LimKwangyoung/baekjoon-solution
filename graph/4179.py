import sys


def bfs():
    result = 0

    que_1 = Ji_Hoon
    que_2 = fires
    while que_1:
        result += 1
        # fire
        new_que = []
        for row, col in que_2:
            coord = ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col))
            for r, c in coord:
                if 0 <= r < R and 0 <= c < C and board[r][c] == '.':
                    board[r][c] = 'F'
                    new_que.append((r, c))
        que_2 = new_que

        # Ji Hoon
        new_que = []
        for row, col in que_1:
            coord = ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col))
            for r, c in coord:
                if r in (-1, R) or c in (-1, C):
                    return result
                if board[r][c] == '.':
                    board[r][c] = 'J'
                    new_que.append((r, c))
        que_1 = new_que
    return 'IMPOSSIBLE'


R, C = map(int, sys.stdin.readline().split())

board = []
Ji_Hoon = []
fires = []
for i in range(R):
    lst = list(sys.stdin.readline().strip())
    board.append(lst)
    for j in range(C):
        if lst[j] == 'J':
            Ji_Hoon.append((i, j))
        elif lst[j] == 'F':
            fires.append((i, j))

print(bfs())
