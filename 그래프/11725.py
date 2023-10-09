import sys
import collections

N = int(sys.stdin.readline())

tree = collections.defaultdict(list)
for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    if v1 == 1:
        tree[1].append(v2)
    elif v2 == 1:
        tree[1].append(v1)
    elif 