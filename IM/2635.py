import sys

N = int(sys.stdin.readline())

result = []
maximum = 0
for next in range(1, N + 1):
    prev = N
    cnt = 0
    lst = []
    while prev >= 0:
        lst.append(str(prev))
        cnt += 1
        prev, next = next, prev - next

    if maximum < cnt:
        maximum = cnt
        result = lst
print(maximum)
print(' '.join(result))
