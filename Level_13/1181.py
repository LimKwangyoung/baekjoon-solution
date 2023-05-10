import sys

N = int(sys.stdin.readline())
word_lst = [sys.stdin.readline().rstrip() for _ in range(N)]

word_lst = list(set(word_lst))  # set is faster than list.
word_lst.sort(key=lambda x: (len(x), x))

for i in word_lst:
    print(i)
