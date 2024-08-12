import sys

N, M = map(int, sys.stdin.readline().split())
heights = [0] + list(map(int, sys.stdin.readline().split()))

start = [0] * (N + 1)
end = [0] * (N + 1)
for _ in range(M):
    a, b, k = map(int, sys.stdin.readline().split())
    start[a] += k
    end[b] += k

weight = 0
for i in range(1, N + 1):
    weight += start[i]
    heights[i] += weight
    weight -= end[i]
print(' '.join(map(str, heights[1:])))
