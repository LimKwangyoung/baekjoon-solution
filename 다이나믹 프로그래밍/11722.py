import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# count when A[i] is included.
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))
