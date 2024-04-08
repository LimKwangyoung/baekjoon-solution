import sys

N, M = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))

if N <= M:
    print(N)
else:
    left, right = 1, N * M
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
        times[i] = left % times[i]
    idx = 0
    while N - total:
        if times[idx] <= 1:
            N -= 1
        idx += 1
    print(idx + 1)

    # cnt = M
    # result = 0
    # rides = times[:]
    # print(f'{result}초: {rides} /// {cnt}명')
    # while N - M:
    #     for i in range(len(rides)):
    #         rides[i] -= 1
    #         if rides[i] == 0:
    #             rides[i] = times[i]
    #             N -= 1
    #             cnt += 1
    #     result += 1
    #     print(f'{result}초: {rides} /// {cnt}명')