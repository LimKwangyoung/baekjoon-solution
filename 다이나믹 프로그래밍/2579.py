import sys

# Solution 1
n = int(sys.stdin.readline())
step_lst = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * n
dp[0] = step_lst[0]
if n >= 2:
    dp[1] = step_lst[0] + step_lst[1]
if n >= 3:
    dp[2] = max(step_lst[0], step_lst[1]) + step_lst[2]

for i in range(3, n):
    dp[i] = max(dp[i - 3] + step_lst[i - 1], dp[i - 2]) + step_lst[i]
print(dp[-1])

# Solution 2
n = int(sys.stdin.readline())
step_lst = [0] * 300  # useful for exception
for i in range(n):
    step_lst[i] = int(sys.stdin.readline())

dp = [0] * 300
dp[0] = step_lst[0]
dp[1] = step_lst[0] + step_lst[1]
dp[2] = max(step_lst[0], step_lst[1]) + step_lst[2]

for i in range(3, n):
    dp[i] = max(dp[i - 3] + step_lst[i - 1], dp[i - 2]) + step_lst[i]
print(dp[n - 1])
