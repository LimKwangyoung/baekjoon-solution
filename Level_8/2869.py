# Solution 1
import math

A, B, V = map(int, input().split())

print(math.ceil((V - A) / (A - B) + 1))

# Solution 2
A, B, V = map(int, input().split())

num = (V - A) / (A - B) + 1
print(int(num) if num == int(num) else int(num) + 1)  # faster than the ceil function
