import sys
import bisect

N, H = map(int, sys.stdin.readline().split())

up, down = [], []
for _ in range(N // 2):
    down.append(int(sys.stdin.readline()))
    up.append(int(sys.stdin.readline()))
up.sort()
down.sort()

minimum = float('inf')
cnt = 0
for h in range(1, H + 1):
    down_cnt = N // 2 - bisect.bisect_right(down, h - 1)
    up_cnt = N // 2 - bisect.bisect_right(up, H - h)
    tmp = down_cnt + up_cnt
    if tmp < minimum:
        minimum = tmp
        cnt = 1
    elif tmp == minimum:
        cnt += 1
print(minimum, cnt)
