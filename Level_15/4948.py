import sys

num_lst = [False, False] + [True] * (2 * 123456 - 1)
while True:
    n = int(sys.stdin.readline())
    if n <= 0:
        break

    for i in range(2, 2 * n + 1):
        if num_lst[i] is True:
            for j in range(2 * i, 2 * n + 1, i):
                num_lst[j] = False
    print(sum(num_lst[n + 1:2 * n + 1]))
