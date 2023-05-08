import sys

N = int(sys.stdin.readline())
coord_lst = []

for _ in range(N):
    xy = sys.stdin.readline().split()
    coord_lst.append(xy)
coord_lst.sort()

for xy in coord_lst:
    print(xy[0], xy[1])
