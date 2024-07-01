import sys


def divide(pl: int, pr: int) -> int:
    global result

    if pl == pr:
        return nums[pl]

    max_idx, maximum = -1, float('-inf')
    for idx in range(pl, pr + 1):
        if maximum < nums[idx]:
            max_idx = idx
            maximum = nums[idx]

    left = divide(pl, max_idx - 1) if pl <= max_idx - 1 else maximum
    right = divide(max_idx + 1, pr) if max_idx + 1 <= pr else maximum
    result += (maximum - left) + (maximum - right)

    return maximum


n = int(sys.stdin.readline())

nums = [int(sys.stdin.readline())]
length = 1
for _ in range(n - 1):
    tmp = int(sys.stdin.readline())
    if nums[-1] != tmp:
        nums.append(tmp)
        length += 1

result = 0
divide(pl=0, pr=length - 1)
print(result)
