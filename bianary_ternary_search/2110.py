import sys

N, C = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(N)]

house.sort()
start, end = 1, (house[-1] - house[0]) // (C - 1)
while start <= end:
    mid = (start + end) // 2

    current = house[0]
    cnt = 1
    for i in range(1, len(house)):
        if house[i] - current >= mid:
            current = house[i]
            cnt += 1

    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1
print(end)
