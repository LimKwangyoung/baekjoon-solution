import sys

code = sys.stdin.readline().rstrip()

dp = [[0, 0] for _ in range(len(code))]  # [new code, tens digit code]
if code == '0':
    print(0)
else:
    dp[0] = [1, 0]
    for i in range(1, len(code)):
        dp[i][0] = sum(dp[i - 1])  # case of new code
        if 1 <= int(code[i - 1] + code[i]) <= 26:  # case of tens digit code
            dp[i][1] = dp[i - 1][0]
    print(sum(dp[-1]) % 1000000)
