import sys

N, M = map(int, sys.stdin.readline().split())
A = set(sys.stdin.readline().split())
B = set(sys.stdin.readline().split())
C = A.intersection(B)

print(len(A) + len(B) - 2 * len(C))
