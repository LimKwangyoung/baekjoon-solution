import sys

E, S, M = map(int, sys.stdin.readline().split())

E -= 1
S -= 1
M -= 1

e, s, m = 0, 0, 0
year = 1
while (e, s, m) != (E, S, M):
    e = (e + 1) % 15
    s = (s + 1) % 28
    m = (m + 1) % 19
    year += 1
print(year)
