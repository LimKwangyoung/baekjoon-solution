import sys
# import math

N, M, K = map(int, sys.stdin.readline().split())

dp = [[0] * (N + M + 1) for _ in range(N + M + 1)]
dp[0][0] = 1

for i in range(1, N + M + 1):
    for j in range(N + M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

# if math.factorial(N + M) // (math.factorial(N) * math.factorial(M)) < K:
if dp[N + M][N] < K:
    print(-1)
else:
    result = ''
    while K:
        if not N:
            result += 'z' * M
            break

        if not M:
            result += 'a' * N
            break

        # cnt = math.factorial(N - 1 + M) // (math.factorial(N - 1) * math.factorial(M))
        cnt = dp[N - 1 + M][N - 1]
        if cnt >= K:
            result += 'a'
            N -= 1
        else:
            result += 'z'
            M -= 1
            K -= cnt
    print(result)
