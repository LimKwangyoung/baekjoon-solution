import sys

T = int(sys.stdin.readline())

cnt_lst = [0, 1, 2, 4] + [0] * 8
for i in range(4, 12):
    cnt_lst[i] = cnt_lst[i - 3] + cnt_lst[i - 2] + cnt_lst[i - 1]

for _ in range(T):
    print(cnt_lst[int(sys.stdin.readline())])
