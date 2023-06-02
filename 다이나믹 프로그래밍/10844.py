import sys

N = int(sys.stdin.readline())

cnt_lst = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for _ in range(N - 1):
    lst = [0] * 10
    lst[0] = cnt_lst[1]
    for i in range(1, 9):
        lst[i] = cnt_lst[i - 1] + cnt_lst[i + 1]
    lst[9] = cnt_lst[8]

    cnt_lst = lst
print(sum(cnt_lst) % 1000000000)
