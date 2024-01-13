import sys
import math


def star(k) -> list:
    if k == 0:
        return ['  *  ', ' * * ', '*****']

    result = []

    prev = star(k - 1)
    n = len(prev)
    for i in prev:
        result.append(' ' * n + i + ' ' * n)
    for i in prev:
        result.append(i + ' ' + i)

    return result


K = int(math.log2(int(sys.stdin.readline()) // 3))
print('\n'.join(star(K)))
