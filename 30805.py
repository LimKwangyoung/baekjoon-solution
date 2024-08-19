import sys
import collections
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A_index = collections.defaultdict(deque)
B_index = collections.defaultdict(deque)

for i, val in enumerate(A):
    A_index[val].append(i)

for i, val in enumerate(B):
    B_index[val].append(i)

result = ''
last_A_idx = last_B_idx = -1
for num in sorted(A, reverse=True):
    if num in B_index:
        tmp = A_index[num].popleft()
        if last_A_idx < tmp:
            while len(B_index[num]) > 0 and B_index[num][0] < last_B_idx:
                B_index[num].popleft()
            if len(B_index[num]) != 0:
                last_A_idx = tmp
                last_B_idx = B_index[num].popleft()
                result += str(num)

print(len(result))
if len(result) > 0:
    print(' '.join(result))

"""
6
5 4 3 1 5 3
7
5 2 1 3 5 4 3
"""
