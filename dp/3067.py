import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = [0] * (M + 1)
    for i in coins:
        dp[i] += 1
        for j in range(i + 1, M + 1):
            dp[j] += dp[j - i]
    print(dp[M])
