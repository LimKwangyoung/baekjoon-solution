import sys

E, S, M = map(int, sys.stdin.readline().split())

if (E, S, M) == (1, 1, 1):
    print(1)
else:
    e, s, m = E + 1, S + 1, M + 1
    year = 2

    while (e, s, m) != (E, S, M):
        if e == 15:
            e = 1
        else:
            e += 1

        if s == 28:
            s = 1
        else:
            s += 1

        if m == 19:
            m = 1
        else:
            m += 1
        year += 1
    print(year)
