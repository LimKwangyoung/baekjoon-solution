import sys

# Solution 1
code = sys.stdin.readline().rstrip()

dp = [[0, 0] for _ in range(len(code))]  # [add new code, connect tens digit code]

if code[0] != '0':
    dp[0][0] = 1

for i in range(1, len(code)):
    # case of adding new code
    if code[i] != '0':
        dp[i][0] = sum(dp[i - 1])
    # case of connecting tens digit code
    if 10 <= int(code[i - 1]) * 10 + int(code[i]) <= 26:
        dp[i][1] = dp[i - 1][0]
print(sum(dp[-1]) % 1000000)

# Solution 2

code = '0' + sys.stdin.readline().rstrip()
dp = [0] * len(code)

if code[1] != '0':
    dp[0] = 1
    dp[1] = 1

for i in range(2, len(code)):
    # case of adding new code
    if code[i] != '0':
        dp[i] += dp[i - 1]
    # case of connecting tens digit code
    if 10 <= int(code[i - 1]) * 10 + int(code[i]) <= 26:
        dp[i] += dp[i - 2]
print(dp[-1] % 1000000)
