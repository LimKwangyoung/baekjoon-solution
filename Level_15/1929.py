import sys


# Solution 1
def primenumber(num: int) -> bool:
    if num <= 1:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


M, N = map(int, sys.stdin.readline().split())

if M <= 2:
    print(2)
if M % 2 == 0:
    print('\n'.join(str(i) for i in range(M + 1, N + 1, 2) if primenumber(i)))
else:
    print('\n'.join(str(i) for i in range(M, N + 1, 2) if primenumber(i)))


# Solution 2 (Sieve of Eratosthenes)
M, N = map(int, sys.stdin.readline().split())

num_lst = [False, False] + [True] * (N - 1)  # it starts at 0.
i = 2
while i * i <= N:
    if num_lst[i]:
        for j in range(2 * i, N + 1, i):
            num_lst[j] = False  # it is faster than Solution 1.
    if i == 2:
        i += 1
    else:  # only handle odd numbers.
        i += 2

print('\n'.join(str(i) for i in range(M, N + 1) if num_lst[i]))
