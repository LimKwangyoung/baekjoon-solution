import sys
import math

# Solution 1
N = int(sys.stdin.readline())

num = str(math.factorial(N))
cnt = 0
for i in num[::-1]:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)

# Solution 2
N = int(sys.stdin.readline())

print(N // 5 + N // 25 + N // 125)
