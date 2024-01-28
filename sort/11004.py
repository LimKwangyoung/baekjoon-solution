import sys

N, K = map(int, sys.stdin.readline().split())
num_lst = list(map(int, sys.stdin.readline().split()))

num_lst.sort()
print(num_lst[K - 1])
