import sys

N = int(sys.stdin.readline())
card_lst = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N + 1)]  # maximum price of i cards
for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], card_lst[j] + dp[i - j])
print(dp[N])
