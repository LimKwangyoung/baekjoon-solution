import sys

# Solution 1
binary = sys.stdin.readline().rstrip()

result = ''
num = 0
for i in range(len(binary), 0, -1):
    if binary[-1 * i] == '1':
        num += 2**((i - 1) % 3)
    if i % 3 == 1:
        result += str(num)
        num = 0
print(result)

# Solution 2 (built-in function)
binary = sys.stdin.readline().rstrip()

print(oct(int(binary, 2))[2:])
