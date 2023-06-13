import sys

# Solution 1
N = int(sys.stdin.readline())

# count of the last number from 0 to 9.
dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for _ in range(2, N + 1):
    temp = dp[:]
    for i in range(1, 10):
        dp[i] = sum(temp[:i + 1])
print(sum(dp) % 10007)

# Solution 2
N = int(sys.stdin.readline())

# count of the last number from 0 to 9.
dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for _ in range(2, N + 1):
    for i in range(1, 10):
        dp[i] += dp[i - 1]
print(sum(dp) % 10007)
