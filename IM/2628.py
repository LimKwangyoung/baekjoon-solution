import sys

N, M = map(int, sys.stdin.readline().split())

cuts = [[], []]
for _ in range(int(sys.stdin.readline())):
    mode, line = map(int, sys.stdin.readline().split())
    cuts[mode].append(line)
for i in cuts:
    i.sort()

