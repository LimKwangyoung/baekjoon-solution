import sys
import collections

# Solution 1
N = int(sys.stdin.readline())

num_dict = {}
for _ in range(N):
    num = int(sys.stdin.readline())
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

lst = []
for i in num_dict:
    lst.append((i, num_dict[i]))
lst.sort(key=lambda x: (-x[1], x[0]))
print(lst[0][0])

# Solution 2
N = int(sys.stdin.readline())
num_lst = [int(sys.stdin.readline()) for _ in range(N)]

lst = collections.Counter(num_lst).most_common()
lst.sort(key=lambda x: (-x[1], x[0]))
print(lst[0][0])
