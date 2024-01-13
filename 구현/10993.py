import sys


def star(n: int) -> list:
    def forward() -> None:
        result.append('*')
        for i in range(1, num):
            result.append('*' + ' ' * (2 * i - 1) + '*')
        for i in range(num):
            result.append('*' + ' ' * (2 * i) + prev[i] + ' ' * (2 * i) + '*')
        result.append('*' * (4 * num + 1))

    def backward() -> None:
        result.append('*' * (4 * num + 1))
        for i in range(num):
            result.append('*' + ' ' * (2 * (num - 1 - i)) + prev[i] + ' ' * (2 * (num - 1 - i)) + '*')
        for i in range(1, num):
            result.append('*' + ' ' * (2 * (num - 1 - i) + 1) + '*')
        result.append('*')

    if n == 1:
        return ['*']

    result = []

    prev = star(n - 1)
    num = len(prev)
    if n % 2:
        forward()
    else:
        backward()

    return result


N = int(sys.stdin.readline())

stars = star(N)
if N % 2:
    for idx in range(len(stars)):
        print(' ' * (len(stars) - 1 - idx) + stars[idx])
else:
    for idx in range(len(stars)):
        print(' ' * idx + stars[idx])
