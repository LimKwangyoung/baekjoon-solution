import sys
import bisect

M, N, L = map(int, sys.stdin.readline().split())
shoots = sorted(list(map(int, sys.stdin.readline().split())))

result = 0
for _ in range(N):
    row, col = map(int, sys.stdin.readline().split())

    idx = bisect.bisect_left(shoots, row)
    if idx >= M or shoots[idx] != row:
        idx -= 1

    dist = min(abs(shoots[idx] - row) + col, abs(shoots[idx + 1] - row) + col if idx < M - 1 else float('inf'))
    if dist <= L:
        result += 1
print(result)
