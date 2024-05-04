import sys
import heapq


def dijkstra() -> int:
    def delta() -> tuple:
        coord = ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col))
        for x, y in coord:
            if 0 <= x < N and 0 <= y < N:
                yield x, y

    que = [(costs[0][0], (0, 0))]  # (cost, (row, col))
    while que:
        cost, (row, col) = heapq.heappop(que)

        if costs[row][col] < cost:
            continue

        for r, c in delta():
            new_cost = costs[row][col] + board[r][c]
            if new_cost < costs[r][c]:
                costs[r][c] = new_cost
                if r == c == N - 1:
                    return new_cost
                heapq.heappush(que, (new_cost, (r, c)))


idx = 0
while True:
    N = int(sys.stdin.readline())
    if not N:
        break

    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    costs = [[float('inf')] * N for _ in range(N)]
    costs[0][0] = board[0][0]

    idx += 1
    print(f'Problem {idx}: {dijkstra()}')
