import sys

N = int(sys.stdin.readline())

for i in range(1, N):
    if i == 1:
        print(' ' * (N - i) + '*')
    else:
        print(' ' * (N - i) + '*' + ' ' * (2 * (i - 1) - 1) + '*')
print('*' * (2 * N - 1))
