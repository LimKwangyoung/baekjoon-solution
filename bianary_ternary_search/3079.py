import sys

N, M = map(int, sys.stdin.readline().split())
times = [int(sys.stdin.readline()) for _ in range(N)]

left, right = 0, max(times) * M
while left <= right:
    mid = (left + right) // 2

    total = sum(mid // time for time in times)
    if total < M:
        left = mid + 1
    else:
        right = mid - 1
print(left)
