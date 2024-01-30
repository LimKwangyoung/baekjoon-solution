import sys
import copy
import collections
import itertools

# Solution 1
N, M = map(int, sys.stdin.readline().split())

# initial setting
wall_cnt = 0
virus_lst = []
origin = []
for i in range(N):
    lst = sys.stdin.readline().split()
    for j in range(M):
        if lst[j] == '1':
            wall_cnt += 1
        elif lst[j] == '2':
            virus_lst.append((i, j))
    origin.append(lst)


def main() -> None:
    def bfs(viruses: int):
        board = copy.deepcopy(origin)
        que = collections.deque(virus_lst)

        while que:
            row, col = que.popleft()
            coord = ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1))
            for r, c in coord:
                if 0 <= r < N and 0 <= c < M and board[r][c] == '0':
                    board[r][c] = '2'
                    que.append((r, c))
                    viruses += 1
        return N * M - (wall_cnt + 3) - viruses

    # cases for building 3 walls
    def build_wall(order: int):
        if order == 3:
            global result
            result = max(result, bfs(virus_cnt))
            return

        for x in range(N):
            for y in range(M):
                if origin[x][y] == '0':
                    origin[x][y] = '1'
                    build_wall(order + 1)
                    origin[x][y] = '0'

    build_wall(0)


virus_cnt = len(virus_lst)
result = 0
main()
print(result)

# Solution 2
N, M = map(int, sys.stdin.readline().split())

# initial setting
blanks = []
virus_lst = []
origin = []
for i in range(N):
    lst = sys.stdin.readline().split()
    for j in range(M):
        if lst[j] == '0':
            blanks.append((i, j))
        elif lst[j] == '2':
            virus_lst.append((i, j))
    origin.append(lst)


def bfs() -> int:
    cnt = 0
    board = copy.deepcopy(origin)
    que = collections.deque(virus_lst)
    while que:
        row, col = que.popleft()
        coord = ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1))
        for r, c in coord:
            if 0 <= r < N and 0 <= c < M and board[r][c] == '0':
                board[r][c] = '2'
                que.append((r, c))
                cnt += 1
    return (len(blanks) - 3) - cnt


# cases for building 3 walls
blank_cases = itertools.combinations(blanks, 3)

result = 0
for blank in blank_cases:
    for x, y in blank:
        origin[x][y] = '1'
    result = max(result, bfs())
    for x, y in blank:
        origin[x][y] = '0'
print(result)
