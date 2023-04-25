import sys

num_lst = list(map(int, sys.stdin.readlines()))

num_lst.sort()
print(int(sum(num_lst) / 5))
print(num_lst[2])
