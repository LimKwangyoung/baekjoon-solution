import sys

N = int(sys.stdin.readline())

print('\n'.join(' ' * (N - i) + '*' * (2 * i - 1) for i in range(1, N + 1)))
