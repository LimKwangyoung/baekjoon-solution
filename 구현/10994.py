import sys


def star(n: int) -> list:
    if n == 1:
        return ['*']

    prev = star(n - 1)
    num = len(prev)

    result = ['*' * (num + 4), '*' + ' ' * (num + 2) + '*']
    for i in prev:
        result.append('* ' + i + ' *')
    result += ['*' + ' ' * (num + 2) + '*', '*' * (num + 4)]

    return result


N = int(sys.stdin.readline())

print('\n'.join(star(N)))
