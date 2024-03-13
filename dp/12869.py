import sys
from itertools import permutations
import collections

# Solution 1
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split())) + [0] * (3 - N)

dp = {(0, 0, 0): 0}
for i in range(nums[0] + 1):
    for j in range(nums[1] + 1):
        for k in range(nums[2] + 1):
            for di, dj, dk in permutations((1, 3, 9), 3):
                dp[(i, j, k)] = min(dp.get((i, j, k), float('inf')), dp[(max(i - di, 0)), max(j - dj, 0), max(k - dk, 0)] + 1)
                # if (i, j, k) in dp:
                #     dp[(i, j, k)] = min(dp[(i, j, k)], dp[(max(i - di, 0)), max(j - dj, 0), max(k - dk, 0)] + 1)
                # else:
                #     dp[(i, j, k)] = dp[(max(i - di, 0)), max(j - dj, 0), max(k - dk, 0)] + 1
print(dp[(nums[0], nums[1], nums[2])])

# Solution 2
N = int(sys.stdin.readline())
que = collections.deque([(list(map(int, sys.stdin.readline().split())) + [0] * (3 - N), 0)])

visited = set()
while que:
    [i, j, k], cnt = que.popleft()
    if i == 0 and j == 0 and k == 0:
        print(cnt)
        break

    for di, dj, dk in permutations((1, 3, 9), 3):
        new_i, new_j, new_k = max(i - di, 0), max(j - dj, 0), max(k - dk, 0)
        if (new_i, new_j, new_k) not in visited:
            que.append(([new_i, new_j, new_k], cnt + 1))
            visited.add((new_i, new_j, new_k))
