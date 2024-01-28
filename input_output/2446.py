import sys

N = int(sys.stdin.readline())

print('\n'.join(' ' * (i - 1) + '*' * (2 * (N + 1 - i) - 1) for i in range(1, N + 1)))
print('\n'.join(' ' * (N - i) + '*' * (2 * i - 1) for i in range(2, N + 1)))
