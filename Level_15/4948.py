import sys

# Solution 1
num_lst = [False, False] + [True] * (2 * 123456 - 1)
while True:
    n = int(sys.stdin.readline())
    if n <= 0:
        break

    i = 2
    while i * i <= 2 * n:
        if num_lst[i] is True:
            for j in range(2 * i, 2 * n + 1, i):
                num_lst[j] = False
        i += 1
    print(sum(num_lst[n + 1:2 * n + 1]))


# Solution 2
def prime_list(num: int) -> list:
    if num <= 1:
        return []
    num_lst = [False, False] + [True] * (num - 1)  # it starts at 0.
    i = 3  # only handle odd numbers.
    while i * i <= num:
        if num_lst[i]:
            for j in range(2 * i, num + 1, i):
                num_lst[j] = False
        i += 2
    return [2] + [i for i in range(3, num + 1, 2) if num_lst[i]]


def bin_search(lst: list, key: int) -> int:
    pl, pr = 0, len(lst) - 1

    while pl <= pr:
        pc = (pl + pr) // 2
        if lst[pc] == key:
            return pc + 1
        elif lst[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
    return pl


Prime_List = prime_list(2 * 123456)

while True:
    n = int(sys.stdin.readline())
    if n <= 0:
        break
    print(bin_search(Prime_List, 2 * n) - bin_search(Prime_List, n))  # it is faster than Solution 1.
