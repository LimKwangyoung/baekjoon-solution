import sys

N, M = map(int, sys.stdin.readline().split())
S = {sys.stdin.readline().rstrip() for _ in range(N)}
lst = [sys.stdin.readline().rstrip() for _ in range(M)]

print(sum(1 if i in S else 0 for i in lst))
