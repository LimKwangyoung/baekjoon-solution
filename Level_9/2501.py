N, K = map(int, input().split())

lst = []
i = 1
while i * i <= N:
    if not N % i:
        lst.append(i)
    i += 1
for j in lst[::-1]:
    if j * j == N:
        continue
    lst.append(N // j)

print(lst[K - 1] if K <= len(lst) else 0)  # faster than using try ~ except.
