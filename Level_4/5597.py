attendance = [0] * 30

for _ in range(28):
    num = int(input())
    attendance[num - 1] = 1

for i in range(30):
    if not attendance[i]:
        print(i + 1)