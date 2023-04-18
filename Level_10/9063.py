import sys

N = int(sys.stdin.readline())  # much faster than using input() in this question

x_lst, y_lst = [], []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_lst.append(x)
    y_lst.append(y)
print((max(x_lst) - min(x_lst)) * (max(y_lst) - min(y_lst)))
