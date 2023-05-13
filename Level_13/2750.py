import sys

N = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readlines()))


# bubble sort
def bubble_sort(lst: list, n: int) -> None:
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


# selection sort
def selection_sort(lst: list, n: int) -> None:
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]


# insertion sort
def insertion_sort(lst: list, n: int) -> None:
    for i in range(1, n):
        j = i
        tmp = lst[i]
        while j > 0 and lst[j - 1] > tmp:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = tmp


# print elements by ascending.
bubble_sort(num_lst, N)
selection_sort(num_lst, N)
insertion_sort(num_lst, N)

for num in num_lst:
    print(num)
