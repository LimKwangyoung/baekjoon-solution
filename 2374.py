import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

cnt = 0
stack = [nums[0]]
for i in range(1, n):
    # ascend
    if stack[-1] <= nums[i]:
        if len(stack) == 1:
            cnt += (nums[i] - stack.pop())
            stack.append(nums[i])
        else:
            num = stack.pop()
            if stack[-1] < nums[i]:
                cnt += (nums[i] - num)
                stack.pop()
                stack.append(nums[i])
            else:
                cnt += (nums[i] - num)
                stack.append(nums[i])
    # descend
    else:
        stack.append(nums[i])
# print(stack)
print(cnt + stack[0] - stack[-1])
