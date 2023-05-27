import sys

N = int(sys.stdin.readline())

print('\n'.join(' ' * (N - i) + '* ' * i for i in range(1, N + 1)))
