import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

dp = [1] * N
for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))
