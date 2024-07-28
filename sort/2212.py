import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensors = sorted(list(map(int, sys.stdin.readline().split())))

lst = []
for i in range(1, N):
    lst.append(sensors[i] - sensors[i - 1])
lst.sort()

result = 0
for i in range(N - K):
    result += lst[i]
print(result)
