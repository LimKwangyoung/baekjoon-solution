import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

nums.sort()

i = 0
result = 0
while i + 1 < N:
    if nums[i] == 0 or nums[i] == 1 or nums[i] * nums[i + 1] < 0:
        result += nums[i]
        i += 1
    elif nums[i + 1] == 0 or nums[i] * nums[i + 1] > 0:
        result += nums[i] * nums[i + 1]
        i += 2
if i != N:
    result += nums[i]
print(result)
