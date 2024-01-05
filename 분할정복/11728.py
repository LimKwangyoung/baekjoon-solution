import sys
import collections

N, M = map(int, sys.stdin.readline().split())

lst_a = collections.deque(list(map(int, sys.stdin.readline().split())))
lst_b = collections.deque(list(map(int, sys.stdin.readline().split())))

result = []
while lst_a and lst_b:
    if lst_a[0] < lst_b[0]:
        result.append(lst_a.popleft())
    else:
        result.append(lst_b.popleft())
if lst_a:
    result += lst_a
else:
    result += lst_b

print(' '.join(map(str, result)))
