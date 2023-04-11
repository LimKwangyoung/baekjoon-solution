N, M = map(int, input().split())

ball_lst = []
for i in range(N):
    ball_lst += [i + 1]

for _ in range(M):
    i, j = map(int, input().split())
    ball_lst[i - 1], ball_lst[j - 1] = ball_lst[j - 1], ball_lst[i - 1]

for i in ball_lst:
    print(i, end=' ')