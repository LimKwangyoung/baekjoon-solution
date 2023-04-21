# Solution 1
from itertools import combinations

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))

result = 0
for i in list(combinations(num_lst, 3)):
    # sum for each combination.
    total = sum(i)
    if result < total <= M:
        result = total
print(result)

# Solution 2
N, M = map(int, input().split())
num_lst = list(map(int, input().split()))

num_lst.sort(reverse=True)
result = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            # sum for each case.
            total = num_lst[i] + num_lst[j] + num_lst[k]  # faster than Solution 1 (using module).
            if result < total <= M:
                result = total
print(result)
