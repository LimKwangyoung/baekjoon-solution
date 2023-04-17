M = int(input())
N = int(input())

total = 0
minimum = 0
for num in range(M, N + 1):
    if num == 1:
        continue
    i = 2
    while i * i <= num:
        if not num % i:
            break
        i += 1
    else:
        if minimum <= 0:
            minimum = num
        total += num
print(f'{total}\n{minimum}' if total > 0 else -1)
