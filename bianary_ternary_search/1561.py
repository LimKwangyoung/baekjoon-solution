import sys

N, M = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))

if N <= M:
    print(N)
else:
    left, right = 1, 30 * N
    N -= M
    while left <= right:
        mid = (left + right) // 2
        num = sum(mid // n for n in times)

        if num >= N:
            right = mid - 1
        else:
            left = mid + 1

    left -= 1
    total = 0
    for i in range(M):
        total += (left // times[i])
        times[i] -= left % times[i]

    idx = -1
    ans = N - total
    while ans:
        idx += 1
        if times[idx] <= 1:
            ans -= 1
    print(idx + 1)
