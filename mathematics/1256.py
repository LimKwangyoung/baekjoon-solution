import sys
import math

N, M, K = map(int, sys.stdin.readline().split())

if math.factorial(N + M) // (math.factorial(N) * math.factorial(M)) < K:
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

        cnt = math.factorial(N - 1 + M) // (math.factorial(N - 1) * math.factorial(M))
        if cnt >= K:
            result += 'a'
            N -= 1
        else:
            result += 'z'
            M -= 1
            K -= cnt
    print(result)
