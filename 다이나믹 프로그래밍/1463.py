import sys

# Solution 1 (BottomUP)
N = int(sys.stdin.readline())
cnt_lst = [0] * (N + 1)  # it starts at 1.

for i in range(2, N + 1):
    # case not for a multiple of 2 and 3.
    cnt_lst[i] = cnt_lst[i - 1] + 1
    # case for a multiple of 2.
    if i % 2 == 0:
        cnt_lst[i] = min(cnt_lst[i // 2] + 1, cnt_lst[i])
    # case for a  multiple of 3.
    if i % 3 == 0:
        cnt_lst[i] = min(cnt_lst[i // 3] + 1, cnt_lst[i])

print(cnt_lst[N])

# Solution 2 (TopDown: recursion)
N = int(sys.stdin.readline())
cnt_dict = {1: 0}


def topdown(num: int) -> int:  # it is faster than Solution 1.
    if num in cnt_dict:
        return cnt_dict[num]

    # case for a multiple of 6.
    if num % 6 == 0:
        cnt_dict[num] = min(topdown(num // 2), topdown(num // 3)) + 1
    # case for a multiple of 2.
    elif num % 2 == 0:
        cnt_dict[num] = min(topdown(num // 2), topdown(num - 1)) + 1
    # case for a multiple of 3.
    elif num % 3 == 0:
        cnt_dict[num] = min(topdown(num // 3), topdown(num - 1)) + 1
    # case not for a multiple of 2 and 3.
    else:
        cnt_dict[num] = topdown(num - 1) + 1

    return cnt_dict[num]


print(topdown(N))

# Solution 3 (TopDown: stack)
N = int(sys.stdin.readline())
cnt_dict = {1: 0}


def case(num: int) -> tuple:
    if num % 6 == 0:
        return num // 2, num // 3
    elif num % 2 == 0:
        return num // 2, num - 1
    elif num % 3 == 0:
        return num // 3, num - 1
    else:
        return num - 1, num - 1


stack_lst = [N]  # it is faster than Solution 1.
while stack_lst:
    n = stack_lst[-1]
    if n in cnt_dict:
        stack_lst.pop(-1)
        continue

    a, b = case(n)
    if a in cnt_dict and b in cnt_dict:
        cnt_dict[n] = min(cnt_dict[a], cnt_dict[b]) + 1
        stack_lst.pop(-1)
        continue
    if a not in cnt_dict:
        stack_lst.append(a)
    if b not in cnt_dict and a != b:
        stack_lst.append(b)

print(cnt_dict[N])
