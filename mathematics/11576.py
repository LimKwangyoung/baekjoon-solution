import sys


A, B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
A_lst = list(map(int, sys.stdin.readline().split()))

decimal_num = sum([A_lst[i] * A**(m - 1 - i) for i in range(m)])

result = []
while decimal_num != 0:
    decimal_num, i = divmod(decimal_num, B)
    result.append(str(i))
print(' '.join(result[::-1]))
