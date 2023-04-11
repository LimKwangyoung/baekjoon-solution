N, M = map(int, input().split())

ball_lst = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    ball_lst[i - 1:j] = [k] * (j - i + 1)

for i in ball_lst:
    print(i, end=' ')