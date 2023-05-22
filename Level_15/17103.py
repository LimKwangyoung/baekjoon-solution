import sys


def get_prime_list(num: int) -> list:
    if num <= 1:
        return []
    num_lst = [False, False] + [True] * (num - 1)
    i = 3
    while i * i <= num:
        if num_lst[i]:
            for j in range(2 * i, num + 1, i):
                num_lst[j] = False
        i += 2
    return [i for i in range(3, num + 1, 2) if num_lst[i]]  # it starts at 3.


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


# Solution 1
PrimeList = get_prime_list(1000000)

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    if N == 4:
        print(1)
        continue

    cnt = 0
    left, right = 0, bin_search(PrimeList, N) - 1  # pointer is faster than set.
    while left <= right:
        if PrimeList[left] + PrimeList[right] == N:
            cnt += 1
            left += 1
            right -= 1
        elif PrimeList[left] + PrimeList[right] < N:
            left += 1
        else:
            right -= 1
    print(cnt)

# Solution 2
PrimeList = get_prime_list(1000000)

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    if N == 4:
        print(1)
        continue

    PrimeSet = set(PrimeList[:bin_search(PrimeList, N)])
    partition = set()
    for p in PrimeSet:
        if N - p in PrimeSet and N - p not in partition:
            partition.add(p)
    print(len(partition))
