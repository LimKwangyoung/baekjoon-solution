import sys

# Sieve of Eratosthenes
eratosthenes_lst = [False, False] + [True] * 999999
i = 2
while i * i <= 1000000:
    if eratosthenes_lst[i]:
        for j in range(2 * i, 1000001, i):
            eratosthenes_lst[j] = False
    if i == 2:
        i += 1
    else:
        i += 2


def goldbach(num: int) -> None:
    for idx in range(3, num // 2 + 1):
        if eratosthenes_lst[idx] and eratosthenes_lst[num - idx]:
            print(f'{num} = {idx} + {num - idx}')
            return
    print("Goldbach's conjecture is wrong.")
    return


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    goldbach(n)
