import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# count when A[i] is included.
dp = A[:]

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + A[i], dp[i])
print(max(dp))
