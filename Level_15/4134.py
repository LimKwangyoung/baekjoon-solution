import sys


def primenumber(num: int) -> bool:
    if num <= 1:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    while True:
        if primenumber(n):
            print(n)
            break
        n += 1
