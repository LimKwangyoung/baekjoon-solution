import sys

N = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readlines()))

# counting sort
minimum, maximum = min(num_lst), max(num_lst)
count_lst = [0] * (maximum - minimum + 1)
result_lst = [0] * N

for num in num_lst:
    count_lst[num - minimum] += 1
for idx in range(maximum - minimum):
    count_lst[idx + 1] += count_lst[idx]

for num in num_lst:
    idx = count_lst[num - minimum]
    result_lst[idx - 1] = num
    count_lst[num - minimum] -= 1
print(result_lst)
