import sys

N, k = map(int, sys.stdin.readline().split())
score_lst = list(map(int, sys.stdin.readline().split()))

score_lst.sort(reverse=True)
print(score_lst[k - 1])
