# Solution 1
N = int(input())

num = 1
while num < N:
    total = num
    for i in str(num):
        total += int(i)
    if total == N:
        print(num)
        break
    num += 1
else:
    print(0)

# Solution 2
N = int(input())

num = max(1, N - len(str(N)) * 9)  # faster than Solution 1.
while num < N:
    total = num
    for i in str(num):
        total += int(i)
    if total == N:
        print(num)
        break
    num += 1
else:
    print(0)
