import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    score_lst = [list(map(int, sys.stdin.readline().split())), list(map(int, sys.stdin.readline().split()))]

    for i in range(1, n):
        if i == 1:
            score_lst[0][i] += score_lst[1][i - 1]
            score_lst[1][i] += score_lst[0][i - 1]
        else:
            score_lst[0][i] += max(score_lst[1][i - 2], score_lst[1][i - 1])
            score_lst[1][i] += max(score_lst[0][i - 2], score_lst[0][i - 1])
    print(max(score_lst[0][-1], score_lst[1][-1]))
