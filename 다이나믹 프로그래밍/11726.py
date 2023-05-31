import sys
import math

# Solution 1
n = int(sys.stdin.readline())

result = 0
for i in range(n % 2, n + 1, 2):
    result += math.factorial(i + (n - i) // 2) // (math.factorial(i) * math.factorial((n - i) // 2))
print(result % 10007)

# Solution 2 (BottomUp)
n = int(sys.stdin.readline())

cnt_dict = [0, 1, 2] + [0] * (n - 2)  # it is faster than Solution 1.
for i in range(3, n + 1):
    cnt_dict[i] = cnt_dict[i - 2] + cnt_dict[i - 1]
print(cnt_dict[n] % 10007)

# Solution 3 (BottomUp)
n = int(sys.stdin.readline())

num1, num2 = 1, 1
for _ in range(2, n + 1):
    num1, num2 = num2, num1 + num2  # it is faster than Solution 1.
print(num2 % 10007)
