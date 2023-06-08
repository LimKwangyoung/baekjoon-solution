import sys

n = int(sys.stdin.readline())

wine_lst = []
for _ in range(n):
    wine_lst.append(int(sys.stdin.readline()))

def bottomup(idx: int) -> int:
    maximum = -sys.maxsize

    stack = [(idx, 0, False)]
    while stack:
        idx, total, prev = stack.pop()
        if idx >= n:
            continue
        total += wine_lst[idx]
        if (idx == n - 1) or (idx == n - 2 and prev):
            maximum = max(maximum, total)
            continue

        if prev:
            stack.append((idx + 2, total, False))
            stack.append((idx + 3, total, False))
        else:
            stack.append((idx + 1, total, True))
            stack.append((idx + 2, total, False))

    return maximum


print(max(bottomup(0), bottomup(1)))
