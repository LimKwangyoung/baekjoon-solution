import sys

N = int(sys.stdin.readline())

cnt_lst = [0, 1]
for _ in range(2, N + 1):
    cnt_lst = [cnt_lst[0] + cnt_lst[1], cnt_lst[0]]
print(sum(cnt_lst))
