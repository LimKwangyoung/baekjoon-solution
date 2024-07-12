import sys
import collections


def move(interval: int) -> bool:
    global result, direction

    for __ in range(interval):
        result += 1

        cur_row, cur_col = snake[-1]
        new_row, new_col = cur_row + delta[direction][0], cur_col + delta[direction][1]

        if new_row in (-1, N) or new_col in (-1, N) or board[new_row][new_col] == 2:
            return False

        # move
        if board[new_row][new_col] == 0:
            prev_row, prev_col = snake.popleft()
            board[prev_row][prev_col] = 0

        snake.append((new_row, new_col))
        board[new_row][new_col] = 2
    return True


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N = int(sys.stdin.readline())

board = [[0] * N for _ in range(N)]

# set apples
for _ in range(int(sys.stdin.readline())):
    row, col = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    board[row][col] = 1

# snake location
snake = collections.deque([(0, 0)])
direction = 1
board[0][0] = 2

result = 0

# snake information
prev_X = 0
for _ in range(int(sys.stdin.readline())):
    X, C = sys.stdin.readline().split()

    if not move(int(X) - prev_X):
        print(result)
        break

    prev_X = int(X)
    if C == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
else:
    if not move(10000):
        print(result)
