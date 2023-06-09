import sys

n = int(sys.stdin.readline())

wine_lst = []
for _ in range(n):
    wine_lst.append(int(sys.stdin.readline()))

total_lst = [0] * n

total_lst[0] = wine_lst[0]
total_lst[1] = wine_lst[0] + wine_lst[1]
total_lst[2] = max(wine_lst[0] + wine_lst[2], wine_lst[1] + wine_lst[2], total_lst[1])
for i in range(3, n):
    total_lst[i] = max(total_lst[i - 3] + wine_lst[i - 1] + wine_lst[i], total_lst[i - 2] + wine_lst[i], total_lst[i - 1])
print(max(total_lst))
