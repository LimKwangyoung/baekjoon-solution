import sys

N = int(sys.stdin.readline())

print('\n'.join('*' * i + ' ' * (2 * N - 2 * i) + '*' * i for i in range(1, N + 1)))
print('\n'.join('*' * i + ' ' * (2 * N - 2 * i) + '*' * i for i in range(N - 1, 0, -1)))
