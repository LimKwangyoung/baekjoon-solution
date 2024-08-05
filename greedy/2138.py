import sys


def transform(cur: list):
    total = 0
    for i in range(N - 2):
        if cur[i] != target[i]:
            cur[i] = change[cur[i]]
            cur[i + 1] = change[cur[i + 1]]
            cur[i + 2] = change[cur[i + 2]]
            total += 1
    return total if cur == target else float('inf')


N = int(sys.stdin.readline())
current = list(sys.stdin.readline().strip())
target = list(sys.stdin.readline().strip())

change = {'0': '1', '1': '0'}

if N == 2:
    result = min(
        transform(current[:]),
        transform([change[current[0]], change[current[1]]]) + 1
    )
elif N == 3:
    result = min(
        transform(current[:]),
        transform([change[current[0]], change[current[1]], current[2]]) + 1,
        transform([current[0], change[current[-2]], change[current[-1]]]) + 1,
        transform([change[current[0]], current[1], change[current[2]]]) + 2
    )
else:
    result = min(
        transform(current[:]),
        transform([change[current[0]], change[current[1]]] + current[2:][:]) + 1,
        transform(current[:-2][:] + [change[current[-2]], change[current[-1]]]) + 1,
        transform([change[current[0]], change[current[1]]] + current[2:-2][:] + [change[current[-2]], change[current[-1]]]) + 2
    )
print(-1 if result == float('inf') else result)
