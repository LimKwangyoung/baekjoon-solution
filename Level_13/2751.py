import sys

N = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readlines()))


# quick sort
def quick_sort(lst: list, n: int) -> None:
    def _quick_sort(left: int, right: int) -> None:
        """quick sort from lst[left] to lst[right]."""
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
            _quick_sort(left, pr)
        if pl < right:
            _quick_sort(pl, right)

    _quick_sort(0, n - 1)


# merge sort
def merge_sort(lst: list, n: int) -> None:
    def _merge_sort(left: int, right: int) -> None:
        """merge sort from lst[left] to lst[right]."""
        if left < right:
            center = (left + right) // 2

            _merge_sort(left, center)
            _merge_sort(center + 1, right)

            buff_idx = buff_right = 0  # index for buffer.
            lst_idx = merge_idx = left  # index for lst.

            # make a buffer from lst[left] to lst[center].
            while lst_idx <= center:
                buff[buff_right] = lst[lst_idx]
                buff_right += 1
                lst_idx += 1

            # merge buffer and an array from lst[center + 1] to lst[right].
            while lst_idx <= right and buff_idx < buff_right:
                if buff[buff_idx] <= lst[lst_idx]:
                    lst[merge_idx] = buff[buff_idx]
                    buff_idx += 1
                else:
                    lst[merge_idx] = lst[lst_idx]
                    lst_idx += 1
                merge_idx += 1

            # copy only the rest of the buffer.
            while buff_idx < buff_right:
                lst[merge_idx] = buff[buff_idx]
                merge_idx += 1
                buff_idx += 1

    buff = [None] * n
    _merge_sort(0, n - 1)
    del buff


# heap sort
def heap_sort(lst: list, n: int) -> None:
    def _heap_sort(left: int, right: int):
        """
        make a heap from lst[left] to lst[right].
        parent index: (i - 1) // 2
        left child index: i * 2 + 1
        right child index: i * 2 + 2
        """
        temp = lst[left]

        parent = left
        while parent < (right - 1) // 2 + 1:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and lst[cl] < lst[cr] else cl
            if temp >= lst[child]:
                break
            lst[parent] = lst[child]
            parent = child
        lst[parent] = temp

    # make an initial heap.
    for i in range((n - 2) // 2, -1, -1):
        _heap_sort(i, n - 1)

    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        _heap_sort(0, i - 1)


# print elements by ascending.
num_lst.sort()
quick_sort(num_lst, N)
merge_sort(num_lst, N)
heap_sort(num_lst, N)

print('\n'.join(map(str, num_lst)))
