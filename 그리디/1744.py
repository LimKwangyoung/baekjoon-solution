import sys

# Solution 1
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

nums.sort()

result = 0
left, right = 0, N - 1

# negative
while left < N and nums[left] < 0:
    if left + 1 >= N or nums[left + 1] > 0:
        result += nums[left]
        left += 1
    else:
        result += nums[left] * nums[left + 1]
        left += 2

# positive
while right >= left and nums[right] > 0:
    if right - 1 < left or nums[right] == 1 or nums[right - 1] == 1:
        result += nums[right]
        right -= 1
    else:
        result += nums[right] * nums[right - 1]
        right -= 2

print(result)

# Solution 2
N = int(sys.stdin.readline())

result = 0
positive, negative = [], []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 1:
        positive.append(num)
    elif num == 1:
        result += num
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

if len(positive) % 2:
    for i in range(0, len(positive) - 1, 2):
        result += positive[i] * positive[i + 1]
    result += positive[-1]
else:
    for i in range(0, len(positive), 2):
        result += positive[i] * positive[i + 1]

if len(negative) % 2:
    for i in range(0, len(negative) - 1, 2):
        result += negative[i] * negative[i + 1]
    result += negative[-1]
else:
    for i in range(0, len(negative), 2):
        result += negative[i] * negative[i + 1]

print(result)
