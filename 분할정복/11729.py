import sys


def hanoi(plate: list, start: int, end: int) -> None:
    if not plate:
        return

    for mid in range(1, 4):
        if mid not in (start, end):
            break
    hanoi(plate[:-1], start, mid)
    result.append((start, end))
    hanoi(plate[:-1], mid, end)


K = int(sys.stdin.readline())

result = []
hanoi(list(range(1, K + 1)), 1, 3)

print(len(result))
for i, j in result:
    print(i, j)
