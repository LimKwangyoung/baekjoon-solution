import sys

N = int(sys.stdin.readline())
x_lst = list(map(int, sys.stdin.readline().split()))

sort_lst = sorted(set(x_lst))
sort_dict = {x: idx for idx, x in enumerate(sort_lst)}  # time complexity of dict is O(1).

print(' '.join(map(str, [sort_dict[i] for i in x_lst])))  # list comprehension is faster than for loop.
