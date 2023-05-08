import sys

# Solution 1
N = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readlines()))  # it causes out of memory.

# counting sort
minimum, maximum = min(num_lst), max(num_lst)
count_lst = [0] * (maximum - minimum + 1)

for num in num_lst:
    count_lst[num - minimum] += 1

for i in range(maximum - minimum + 1):
    if count_lst[i] != 0:
        for _ in range(count_lst[i]):
            print(minimum + i)

# Solution 2
N = int(sys.stdin.readline())
count_lst = [0] * 10000

# counting sort
for _ in range(N):
    num = int(sys.stdin.readline())
    count_lst[num - 1] += 1

for i in range(10000):
    if count_lst[i] != 0:
        for _ in range(count_lst[i]):
            print(i + 1)
