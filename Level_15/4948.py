import sys

# Solution 1
num_lst1 = [False, False] + [True] * (2 * 123456 - 1)
while True:
    n = int(sys.stdin.readline())
    if n <= 0:
        break

    i1 = 2
    while i1 * i1 <= 2 * n:
        if num_lst1[i1] is True:
            for j1 in range(2 * i1, 2 * n + 1, i1):
                num_lst1[j1] = False
        i1 += 1
    print(sum(num_lst1[n + 1:2 * n + 1]))


# Solution 2
def get_prime_list(num: int) -> list:
    if num <= 1:
        return []
    num_lst2 = [False, False] + [True] * (num - 1)
    i2 = 3  # only handle odd numbers.
    while i2 * i2 <= num:
        if num_lst2[i2]:
            for j2 in range(2 * i2, num + 1, i2):
                num_lst2[j2] = False
        i2 += 2
    return [2] + [i2 for i2 in range(3, num + 1, 2) if num_lst2[i2]]


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


PrimeList = get_prime_list(2 * 123456)

while True:
    n = int(sys.stdin.readline())
    if n <= 0:
        break
    print(bin_search(PrimeList, 2 * n) - bin_search(PrimeList, n))  # it is faster than Solution 1.
