N = int(input())
lst = list(map(int, input().split()))

cnt = 0
for num in lst:
    if num == 1:
        continue
    i = 2
    while i * i <= num:
        if not num % i:
            break
        i += 1
    else:
        cnt += 1
print(cnt)
