import sys


def max_side(idx: int) -> int:
    maximum = 0
    for i in range(6):
        if i not in {bottom, top}:
            maximum = max(maximum, dices[idx][i])
    return maximum


N = int(sys.stdin.readline())
dices = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = 0
opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
for start in range(6):
    total = 0
    bottom, top = start, opposite[start]
    for n in range(N):
        total += max_side(n)
        print(max_side(n))
    break
    result = max(result, total)
print(result)
