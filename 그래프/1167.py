import sys

V = int(sys.stdin.readline())
for _ in range(V):
    lst = list(map(int, sys.stdin.readline().split()))[:-1]
    print(lst)
