import sys

n = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readline().split()))

# maximum sum when num_lst[i] is included.
dp = num_lst[:]
for i in range(1, n):
    dp[i] = max(dp[i - 1] + num_lst[i], dp[i])
print(max(dp))
