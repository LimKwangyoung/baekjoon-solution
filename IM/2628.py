import sys


def cal_maximum(arr: list) -> int:
    result = 0
    for idx in range(1, len(arr)):
        result = max(result, arr[idx] - arr[idx - 1])
    return result


N, M = map(int, sys.stdin.readline().split())

cuts = [[0, M], [0, N]]  # [horizon, vertical]
for _ in range(int(sys.stdin.readline())):
    mode, line = map(int, sys.stdin.readline().split())
    cuts[mode].append(line)
for i in cuts:
    i.sort()

print(cal_maximum(cuts[0]) * cal_maximum(cuts[1]))
