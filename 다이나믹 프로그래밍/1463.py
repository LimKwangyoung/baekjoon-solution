import sys


def three_case(num: int) -> int:
    cnt = 0

    while num != 1:
        if (num - 1) % 3 == 0:
            num -= 1
        elif num % 3 == 0:
            num /= 3
        elif num % 2 == 0:
            num /= 2
        else:
            num -= 1
        cnt += 1
    return cnt


print(three_case(int(sys.stdin.readline())))
