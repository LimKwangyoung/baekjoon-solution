import sys


def attach(horizon: int, board: list, papers: list, total: int) -> None:
    def check() -> list:
        border = [(row + i, col + length) for i in range(length)] \
                 + [(row + length, col + i) for i in range(length)] \
                 + [(row + length, col + length)]
        for i, j in border:
            if not (0 <= i < 10 and 0 <= j < 10) or board[i][j] == '0':
                return []
        return border

    global result
    if total >= result or max(papers) > 5:
        return

    for row in range(horizon, 10):
        for col in range(10):
            if board[row][col] == '1':
                copied = [line.copy() for line in board]
                for length in range(5):
                    ans = check()
                    if ans:
                        for r, c in ans:
                            copied[r][c] = '0'
                        papers[length] += 1
                        attach(horizon=row, board=copied, papers=papers, total=total + 1)
                        papers[length] -= 1
                    else:
                        return
                return
    result = min(result, total)


origin = []
cnt = 0
for _ in range(10):
    tmp = list(sys.stdin.readline().split())
    cnt += tmp.count('0')
    origin.append(tmp)

if cnt == 100:
    print(0)
else:
    result = float('inf')
    attach(horizon=0, board=origin, papers=[0, 0, 0, 0, 0], total=0)
    print(-1 if result == float('inf') else result)
