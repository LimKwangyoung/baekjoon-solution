import sys

N = int(sys.stdin.readline())

works = [0] * (N + 1)
for i in range(1, N + 1):
    time, _, *lst = map(int, sys.stdin.readline().split())
    works[i] = [lst, time]

completed = [0] * (N + 1)
for i in range(1, N + 1):
    if not works[i][0]:
        completed[i] = works[i][1]
    else:
        tmp = max(completed[j] for j in works[i][0])
        completed[i] = tmp + works[i][1]
print(max(completed))
