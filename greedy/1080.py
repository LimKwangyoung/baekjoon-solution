import sys


def reverse(row: int, col: int) -> None:
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            A[r][c] = (A[r][c] + 1) % 2


N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

cnt = 0
if (N < 3 or M < 3) and A != B:
    print(-1)
else:
    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                reverse(row=i, col=j)
                cnt += 1
    print(cnt if A == B else -1)
