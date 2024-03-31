import sys


def dfs(row: int, col: int, level: int, total: float) -> None:
    global alls, simples

    if level == N:
        alls += total
        simples += total
        return

    for i in range(4):
        if prob[i]:
            new_row, new_col = row + delta[i][0], col + delta[i][1]
            if visited[new_row][new_col]:
                alls += total * prob[i]
            else:
                visited[new_row][new_col] = True
                dfs(new_row,  new_col, level + 1, total * prob[i])
                visited[new_row][new_col] = False


N, *prob = map(int, sys.stdin.readline().split())
prob = list(map(lambda x: x / 100, prob))

alls = simples = 0
visited = [[False] * 30 for _ in range(30)]
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

visited[15][15] = True
dfs(15, 15, 0, 1)
print(simples / alls)
