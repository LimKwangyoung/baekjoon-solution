import sys

N = int(sys.stdin.readline())

lst = []
while N != 0:
    N, i = divmod(N, -2)
    if i < 0:
        N += 1
        i = 1
    lst.append(str(i))
print(''.join(lst[::-1]) if lst else 0)
