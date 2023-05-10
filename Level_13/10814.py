import sys

N = int(sys.stdin.readline())
member_lst = [sys.stdin.readline().split() for _ in range(N)]

member_lst.sort(key=lambda x: int(x[0]))

for i in member_lst:
    print(i[0], i[1])
