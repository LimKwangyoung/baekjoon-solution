import sys

# Solution 1 (BottomUP)
N = int(sys.stdin.readline())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    # case for subtracting 1.
    dp[i] = dp[i - 1] + 1
    # case for a multiple of 2.
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    # case for a  multiple of 3.
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])

print(dp[N])

# Solution 2 (TopDown: recursion)
N = int(sys.stdin.readline())
dp = {1: 0}


def topdown(num: int) -> int:  # it is faster than Solution 1.
    if num in dp:
        return dp[num]

    # case for a multiple of 6.
    if num % 6 == 0:
        dp[num] = min(topdown(num // 2), topdown(num // 3)) + 1
    # case for a multiple of 2.
    elif num % 2 == 0:
        dp[num] = min(topdown(num // 2), topdown(num - 1)) + 1
    # case for a multiple of 3.
    elif num % 3 == 0:
        dp[num] = min(topdown(num // 3), topdown(num - 1)) + 1
    # case not for a multiple of 2 and 3.
    else:
        dp[num] = topdown(num - 1) + 1

    return dp[num]


print(topdown(N))

# Solution 3 (TopDown: stack)
N = int(sys.stdin.readline())
dp = {1: 0}


def case(num: int) -> tuple:
    if num % 6 == 0:
        return num // 2, num // 3
    elif num % 2 == 0:
        return num // 2, num - 1
    elif num % 3 == 0:
        return num // 3, num - 1
    else:
        return num - 1, num - 1


stack = [N]  # it is faster than Solution 1.
while stack:
    n = stack[-1]  # peak
    if n in dp:
        stack.pop(-1)
        continue

    a, b = case(n)
    if a in dp and b in dp:
        dp[n] = min(dp[a], dp[b]) + 1
        stack.pop(-1)
        continue
    if a not in dp:
        stack.append(a)
    if b not in dp and a != b:
        stack.append(b)

print(dp[N])
