import sys

n = int(sys.stdin.readline())

wine_lst = []
for _ in range(n):
    wine_lst.append(int(sys.stdin.readline()))

dp = [0] * n

dp[0] = wine_lst[0]
dp[1] = wine_lst[0] + wine_lst[1]
dp[2] = max(wine_lst[0] + wine_lst[2], wine_lst[1] + wine_lst[2], dp[1])
for i in range(3, n):
    dp[i] = max(dp[i - 2] + wine_lst[i],  # drink wine_lst[i]: and not drink wine_lst[i - 1]
                dp[i - 3] + wine_lst[i - 1] + wine_lst[i],  # drink wine_lst[i]: and drink wine_lst[i - 1]
                dp[i - 1])  # not drink wine_lst[i]

print(max(dp))
