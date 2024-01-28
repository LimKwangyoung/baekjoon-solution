import sys

K, N = map(int, sys.stdin.readline().split())
lan_lst = [int(sys.stdin.readline()) for _ in range(K)]

start, end = 1, max(lan_lst)
while start <= end:
    mid = (start + end) // 2
    num = sum(i // mid for i in lan_lst)

    if N <= num:
        start = mid + 1
    else:
        end = mid - 1
print(end)
