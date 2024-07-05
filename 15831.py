import sys

"""
10 1 2
WBBWWBWWBW

7 2 4
WBBBBBW
"""

colors = {'B': 0, 'W': 1}

N, B, W = map(int, sys.stdin.readline().split())
rocks = sys.stdin.readline().strip()

result = 0
idx = 0
while idx < N:
    cnt = 0

    info = [0, 0]  # [black, white]
    while info[0] <= B:
        info[rocks[idx]] += 1
        idx += 1
        cnt += 1


