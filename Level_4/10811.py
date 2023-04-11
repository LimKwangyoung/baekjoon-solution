N, M = map(int, input().split())

basket = []
for i in range(N):
    basket += [i + 1]

for _ in range(M):
    i, j = map(int, input().split())
    lst = basket[i - 1:j]
    lst.reverse()
    basket[i - 1:j] = lst

for i in basket:
    print(i, end=' ')