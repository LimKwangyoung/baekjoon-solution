import sys

N = int(sys.stdin.readline())
num_set = set(map(int, sys.stdin.readline().split()))  # time complexity of set is O(1).
M = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readline().split()))

print(' '.join('1' if num in num_set else '0' for num in num_lst))  # list comprehension is faster than for loop.
