N = int(input())
score_lst = list(map(int, input().split()))

maximum = max(score_lst)
total = 0
for i in score_lst:
    total += i / maximum * 100
print(total / N)