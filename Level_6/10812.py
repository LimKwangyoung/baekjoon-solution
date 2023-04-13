N, M = map(int, input().split())
basket_lst = [i + 1 for i in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    basket_lst[i - 1:j] = basket_lst[k - 1:j] + basket_lst[i - 1:k - 1]

for i in basket_lst:
    print(i, end=' ')