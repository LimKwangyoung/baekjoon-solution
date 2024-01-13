import sys

N = int(sys.stdin.readline())

result = ['*' * N + ' ' * (2 * N - 3) + '*' * N]
for i in range(1, N - 1):
    result.append(' ' * i + '*' + ' ' * (N - 2) + '*' + ' ' * ((2 * N - 3) - 2 * i) + '*' + ' ' * (N - 2) + '*')
result += [' ' * (N - 1) + '*' + ' ' * (N - 2) + '*' + ' ' * (N - 2) + '*'] + result[::-1]

print('\n'.join(result))
