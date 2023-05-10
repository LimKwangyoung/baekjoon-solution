import sys

N = int(sys.stdin.readline())
x_lst = list(map(int, sys.stdin.readline().split()))

# Solution 1
sort_lst = sorted(set(x_lst))
sort_dict = {x: idx for idx, x in enumerate(sort_lst)}  # time complexity of dict is O(1).

for i in x_lst:
    print(sort_dict[i], end=' ')

# Solution 2
