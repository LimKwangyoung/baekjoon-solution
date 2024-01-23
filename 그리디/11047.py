import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]

i = -1
cnt = 0
while K > 0:
    quotient, K = divmod(K, coins[i])
    cnt += quotient
    i -= 1
print(cnt)
