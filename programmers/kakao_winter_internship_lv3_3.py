def solution(n, tops):
    dp = [0] * (2 * n + 1)
    dp[0] = 1
    dp[1] = dp[0] * 2 + tops[1 // 2]
    for i in range(2, 2 * n + 1):
        dp[i] += dp[i - 2]
        if i % 2:
            dp[i] += dp[i - 1] * (1 + tops[i // 2])
        else:
            dp[i] += dp[i - 1]
        dp[i] %= 10007
    return dp[-1]
