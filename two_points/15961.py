import sys
import collections

N, d, k, c = map(int, sys.stdin.readline().split())
sushi = [sys.stdin.readline().strip() for _ in range(N)]
coupon = str(c)

tmp = collections.defaultdict(int)
for i in range(k):
    tmp[sushi[i]] += 1
tmp[coupon] += 1

result = 0
left, right = 0, k
while left < N:
    result = max(result, len(tmp))

    tmp[sushi[left]] -= 1
    if not tmp[sushi[left]]:
        del tmp[sushi[left]]
    tmp[sushi[right]] += 1

    left += 1
    right = (right + 1) % N
print(result)
