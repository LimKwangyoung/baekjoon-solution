import string

word = input()
lst = string.ascii_lowercase

for i in lst:
    if i in word:
        print(word.index(i), end=' ')
    else:
        print(-1, end=' ')