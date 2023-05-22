import sys


def get_prime_dict(num: int) -> dict:
    num_dict = {i: True for i in range(3, num + 1, 2)}
    i = 3
    while i * i <= num:
        if num_dict[i]:
            for j in range(2 * i, num + 1, i):
                num_dict[j] = False
        i += 2
    result = {2: True}
    result.update({i: True for i in range(3, num + 1, 2) if num_dict[i]})

    return result


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    prime_dict = get_prime_dict(N - 1)

    if N // 2 in prime_dict:
        cnt = 1
    else:
        cnt = 0

    for i in prime_dict:
        if N - i in prime_dict:
            cnt += 1
    print(cnt // 2)
