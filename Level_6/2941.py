lst = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
word = input()

idx = 0
cnt = 0
while idx < len(word):
    if word[idx:idx + 2] in lst:
        idx += 2
        cnt += 1
    elif word[idx:idx + 3] in lst:
        idx += 3
        cnt += 1
    else:
        idx += 1
        cnt += 1
print(cnt)