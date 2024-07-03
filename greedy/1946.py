import sys

T = int(sys.stdin.readline())

for _ in range(T):
    cnt = 1

    N = int(sys.stdin.readline())
    ranks = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

    best_rank = ranks[0][1]
    for _, rank in ranks[1:]:
        if rank < best_rank:
            cnt += 1
        best_rank = min(best_rank, rank)
    print(cnt)
