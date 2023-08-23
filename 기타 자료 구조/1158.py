import sys
import collections

# Solution 1
N, K = map(int, sys.stdin.readline().split())

que = collections.deque(i for i in range(1, N + 1))
cnt = 1
result = []
while que:
    if cnt == K:
        result.append(que.popleft())
        cnt = 1
        continue
    que.append(que.popleft())
    cnt += 1
print('<' + ', '.join(map(str, result)) + '>')

# Solution 2
N, K = map(int, sys.stdin.readline().split())

num_lst = [i for i in range(1, N + 1)]
result = []
idx = 0
for _ in range(N):
    idx = (idx + (K - 1)) % len(num_lst)  # it is faster than Solution 1.
    result.append(num_lst.pop(idx))
print('<' + ', '.join(map(str, result)) + '>')
