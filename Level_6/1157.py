# Solution 1
word = input()

word_lst = [] # save in upper case
count_lst = []

for i in word:
    alphabet = i.upper()
    if alphabet not in word_lst:
        word_lst.append(alphabet)
        count_lst.append(1)
    else:
        idx = word_lst.index(alphabet)
        count_lst[idx] += 1

maximum = max(count_lst)
max_idx = 0
overlap = False
for i in range(len(count_lst)):
    if count_lst[i] == maximum:
        if overlap:
            print('?')
            break
        max_idx = i
        overlap = True
else:
    print(word_lst[max_idx])

# Solution 2
word = input().upper()

max_cnt = 0
max_alphabet = ''
for i in range(26):
    cnt = word.count(chr(ord('A') + i))
    if max_cnt < cnt:
        max_cnt = cnt
        max_alphabet = chr(ord('A') + i)
    elif max_cnt == cnt:
        max_alphabet = '?'
print(max_alphabet)