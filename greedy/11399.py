import sys

N = int(sys.stdin.readline())
takes = list(map(int, sys.stdin.readline().split()))

takes.sort()
print(sum(takes[i] * (N - i) for i in range(N)))
