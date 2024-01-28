import sys


def count_i(num: int, i: int) -> int:
    result = 0
    i_square = i
    while i_square <= num:
        result += num // i_square
        i_square *= i
    return result


n, m = map(int, sys.stdin.readline().split())

cnt = min(count_i(n, 2) - count_i(m, 2) - count_i(n - m, 2),
          count_i(n, 5) - count_i(m, 5) - count_i(n - m, 5))
print(cnt)
