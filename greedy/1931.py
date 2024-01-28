import sys

N = int(sys.stdin.readline())
lst = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

meetings = sorted(lst, key=lambda x: (x[1], x[0]))

time, cnt = 0, 0
for start, end in meetings:
    if start >= time:
        time = end
        cnt += 1
print(cnt)
