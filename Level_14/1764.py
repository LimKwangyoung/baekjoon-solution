import sys

N, M = map(int, sys.stdin.readline().split())
name_set1 = {sys.stdin.readline().rstrip() for _ in range(N)}
name_set2 = {sys.stdin.readline().rstrip() for _ in range(M)}

name_set3 = sorted(name_set1.intersection(name_set2))
print(len(name_set3))
print('\n'.join(name_set3))
