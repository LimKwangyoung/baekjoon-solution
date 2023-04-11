lst = []

for _ in range(10):
    num = int(input()) % 42
    if num not in lst:
        lst.append(num)

print(len(lst))