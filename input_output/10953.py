import sys

T = int(sys.stdin.readline())

print('\n'.join(str(sum(map(int, sys.stdin.readline().split(',')))) for _ in range(T)))
