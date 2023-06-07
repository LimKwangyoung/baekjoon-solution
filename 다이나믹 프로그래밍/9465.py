import sys


T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split())) + list(map(int, sys.stdin.readline().split()))

    score, max_score = 0, -sys.maxsize
    def bottomup(idx: int) -> int:
        global score
        if idx % 10 == (n - 1):
            return max(score, max_score)

        score += lst[idx]
        if idx % 10 <= 3:
            bottomup((idx + 6) % 10)
            if idx % 10 <= 2:
                bottomup((idx + 7) % 10)
        return score

    print(max(bottomup(0), bottomup(n)))
