import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# count when A[i] is included.
dp_1 = [1] * N  # ascending.
dp_2 = [1] * N  # descending.

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp_1[i] = max(dp_1[j] + 1, dp_1[i])
        if A[::-1][j] < A[::-1][i]:
            dp_2[i] = max(dp_2[j] + 1, dp_2[i])

result = [0] * N
for i in range(N):
    result[i] = dp_1[i] + dp_2[N - 1 - i] - 1
print(max(result))
