import sys


def star(n: int) -> list:
    if n == 1:
        return ['*']
    elif n == 2:
        return ['*****', '*', '* ***', '* * *', '* * *', '*   *', '*****']

    prev = star(n - 1)
    num = len(prev)

    result = ['*' * (num + 2), '*']
    result += ['* ' + prev[0] + '**', '* ' + prev[1] + ' ' * (num - 2) + '*']
    for i in prev[2:]:
        result += [f'* {i} *']
    result += ['*' + ' ' * num + '*', '*' * (num + 2)]

    return result


N = int(sys.stdin.readline())

print('\n'.join(star(N)))
