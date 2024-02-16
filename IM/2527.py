import sys

for _ in range(4):
    a1, b1, a2, b2, c1, d1, c2, d2 = map(int, sys.stdin.readline().split())

    if (a2 < c1 or c2 < a1) or (b2 < d1 or d2 < b1):
        print('d')
    elif a2 == c1 or a1 == c2:
        if b2 == d1 or b1 == d2:
            print('c')
        else:
            print('b')
    elif b2 == d1 or b1 == d2:
        print('b')
    else:
        print('a')
