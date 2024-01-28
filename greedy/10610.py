import sys

N = sys.stdin.readline().strip()

if not sum(map(int, N)) % 3 and '0' in N:
    print(''.join(sorted(N, reverse=True)))
else:
    print(-1)
