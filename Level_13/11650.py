import sys

N = int(sys.stdin.readline())
pair_lst = []

for _ in range(N):
    pair = list(map(int, sys.stdin.readline().split()))
    pair_lst.append(pair)
pair_lst.sort()

for i in pair_lst:
    print(i[0], i[1])
