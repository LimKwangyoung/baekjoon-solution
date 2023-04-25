import sys

N = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readlines()))

# Bubble Sort
for i in range(N - 1):
    for j in range(N - 1 - i):
        if num_lst[j] > num_lst[j + 1]:
            num_lst[j], num_lst[j + 1] = num_lst[j + 1], num_lst[j]

# Selection Sort
for i in range(N - 1):
    min_idx = i
    for j in range(i + 1, N):
        if num_lst[j] < num_lst[min_idx]:
            min_idx = j
    num_lst[i], num_lst[min_idx] = num_lst[min_idx], num_lst[i]

# Insertion Sort
for i in range(1, N):
    j = i
    tmp = num_lst[i]
    while j > 0 and num_lst[j - 1] > tmp:
        num_lst[j] = num_lst[j - 1]
        j -= 1
    num_lst[j] = tmp

for num in num_lst:
    print(num)
