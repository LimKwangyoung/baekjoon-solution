"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
첫째 줄에 알바벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000를 넘지 않는다.
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

Mississipi          ?
zZa                 Z
Z                   Z
baaa                A
"""

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