import sys

N = int(sys.stdin.readline())

cnt_lst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for _ in range(2, N + 1):
    for i in range(1, 10):
        cnt_lst[i] += cnt_lst[i - 1]
print(sum(cnt_lst) % 10007)
