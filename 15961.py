import sys
import collections

N, d, k, c = map(int, sys.stdin.readline().split())
sushi = [sys.stdin.readline().strip() for _ in range(N)]
coupon = str(c)

lst = collections.deque()
i = (-k + 1) % N
for _ in range(k):
    lst.append(sushi[i])
    i = (i + 1) % N

result = float('-inf')
prev = sushi[(i - k) % N]
for i in range(N):
    if prev == coupon:
        result = max(result, len(set(lst) | {prev}))
    else:
        result = max(result, len(set(lst)))
    prev = lst.popleft()
    lst.append(sushi[(i + 1) % N])
print(result)
