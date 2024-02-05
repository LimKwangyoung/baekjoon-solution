import sys


def max_side(idx: int) -> int:
    maximum = 0
    for num in range(6):
        if num not in {bottom, opposite[bottom]}:
            maximum = max(maximum, dices[idx][num])
    return maximum


N = int(sys.stdin.readline())

dices = [[None] * 6 for _ in range(N)]
sides = [[None] * 7 for _ in range(N)]
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(6):
        dices[i][j] = lst[j]
        sides[i][lst[j]] = j

result = 0
opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
for start in range(6):
    total = 0
    for i in range(N):
        if i == 0:
            bottom = start
        else:
            bottom = sides[i][dices[i - 1][opposite[bottom]]]
        total += max_side(i)
    result = max(result, total)
print(result)
