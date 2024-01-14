import sys
import collections


# Solution 1
def hanoi(n: int, start: int, end: int) -> None:
    if n == 1:
        print(f'{start} {end}')
        return

    hanoi(n - 1, start, 6 - start - end)
    print(f'{start} {end}')
    hanoi(n - 1, 6 - start - end, end)


K = int(sys.stdin.readline())

print(2**K - 1)
hanoi(n=K, start=1, end=3)


# Solution 2 (faster than Solution 1)
def hanoi(n: int, start: int, end: int) -> str:
    if n == 1:
        return f'{start} {end}'

    if (n, start, end) in path:
        return path[(n, start, end)]

    # lst: list[str]
    lst = [hanoi(n - 1, start, 6 - start - end), f'{start} {end}', hanoi(n - 1, 6 - start - end, end)]
    path[(n, start, end)] = '\n'.join(lst)

    return path[(n, start, end)]


K = int(sys.stdin.readline())

# dictionary for reducing duplication
path = collections.defaultdict(str)

print(2**K - 1)
print(hanoi(n=K, start=1, end=3))
