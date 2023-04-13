C = int(input())

for _ in range(C):
    score_lst = list(map(int, input().split()))
    avg = sum(score_lst[1:]) / score_lst[0]

    cnt = 0
    for i in score_lst[1:]:
        if i > avg:
            cnt += 1
    print(f'{cnt / score_lst[0] * 100:.3f}%')