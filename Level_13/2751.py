import sys

N = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readlines()))

# built-in function
num_lst.sort()


# quick sort
def qsort(lst: list, left: int, right: int) -> None:
    pl, pr = left, right
    x = lst[(left + right) // 2]

    while pl <= pr:
        while lst[pl] < x:
            pl += 1
        while x < lst[pr]:
            pr -= 1
        if pl <= pr:
            lst[pl], lst[pr] = lst[pr], lst[pl]
            pl += 1
            pr -= 1

    if left < pr:
        qsort(lst, left, pr)
    if pl < right:
        qsort(lst, pl, right)


def quick_sort(lst: list, n: int) -> None:
    qsort(lst, 0, n - 1)


# merge sort

# heap sort

# print elements by ascending.
quick_sort(num_lst, N)

for i in num_lst:
    print(i)
