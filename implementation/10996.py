import sys

N = int(sys.stdin.readline())

for _ in range(N):
    print('* ' * (N - N // 2))
    print(' *' * (N // 2))
