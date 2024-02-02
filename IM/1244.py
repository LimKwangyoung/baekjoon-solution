import sys

N = int(sys.stdin.readline())
switches = [0] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
students = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for sex, num in students:
    if sex == 1:  # male
        for i in range(num, N + 1, num):
            switches[i] = (switches[i] + 1) % 2
    else:  # female
        switches[num] = (switches[num] + 1) % 2
        length = min(num - 1, N - num)
        for i in range(0, length + 1):
            if switches[num - i] == switches[num + i]:
                switches[num - i] = (switches[num - i] + 1) % 2
                switches[num + i] = (switches[num + i] + 1) % 2
            else:
                break
for i in range(1, N + 1):
    print(switches[i], end=' ')
    if not i % 20:
        print()
