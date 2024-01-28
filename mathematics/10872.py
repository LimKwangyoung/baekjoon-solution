import sys
import math

# Solution 1
N = int(sys.stdin.readline())

print(math.factorial(N))

# Solution 2
N = int(sys.stdin.readline())

result = 1
for i in range(1, N + 1):
    result *= i
print(result)
