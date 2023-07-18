import sys

N = int(sys.stdin.readline())
num_lst = [int(sys.stdin.readline()) for _ in range(N)]

num_set = sorted(list(set(num_lst)), reverse=True)
max_num, max_cnt = num_set[0], num_lst.count(num_set[0])
for i in num_set[1:]:
    if num_lst.count(i) > max_cnt:
        max_num = i
print(max_num)
