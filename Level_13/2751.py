import sys

N = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readlines()))

# built-in function
num_lst.sort()

# heap sort

# merge sort

# quick sort
def partition(lst: list) -> None:
    n = len(lst)
    pl, pr = 0, n - 1
    x = lst[n // 2]

    while pl < pr:
        while lst[pl] < x:
            pl += 1
        while x < lst[pr]:
            pr -= 1
        if pl < pr:
            lst[pl], lst[pr] = lst[pr], lst[pl]
            pl += 1
            pr -= 1


# print elements by ascending.
for i in num_lst:
    print(i)
