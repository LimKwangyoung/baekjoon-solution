N = int(input())

cnt = 0
for _ in range(N):
    word = input()
    lst = []

    for i in range(len(word)):
        if word[i] not in lst:
            lst.append(word[i])
        elif word[i] == word[i - 1]:
            continue
        else:
            break
    else:
        cnt += 1
print(cnt)