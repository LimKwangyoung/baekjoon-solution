import sys


# Solution 1
def primenumber(num: int) -> set:
    result_set = {1, num}

    i = 2
    while i * i <= num:
        if num % i == 0:
            result_set.add(i)
            result_set.add(num // i)
        i += 1

    return result_set


T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    gcd = max(primenumber(A).intersection(primenumber(B)))
    print(gcd * (A // gcd) * (B // gcd))

# Solution 2 (Euclidean algorithm)
T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    a, b = A, B

    while a % b != 0:
        a, b = b, a % b  # it is faster than Solution 1.
    print(A * B // b)  # b is GCD.
