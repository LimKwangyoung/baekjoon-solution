import sys

N = int(sys.stdin.readline())

# count of the last number from 0 to 9.
dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for _ in range(N - 1):
    temp = [0] * 10
    temp[0] = dp[1]
    for i in range(1, 9):
        temp[i] = dp[i - 1] + dp[i + 1]
    temp[9] = dp[8]

    dp = temp
print(sum(dp) % 1000000000)
