import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    num_lst = [list(map(int, sys.stdin.readline().split())), list(map(int, sys.stdin.readline().split()))]

    for i in range(n):
        if i == 0:
            continue
        elif i == 1:
            num_lst[0][i] += num_lst[1][0]
            num_lst[1][i] += num_lst[0][0]
        else:
            num_lst[0][i] += max(num_lst[1][i - 2], num_lst[1][i - 1])
            num_lst[1][i] += max(num_lst[0][i - 2], num_lst[0][i - 1])
    print(max(num_lst[0][-1], num_lst[1][-1]))
