string = input()
alphabet_lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

t = 0
for i in string:
    for alphabet in alphabet_lst:
        if i in alphabet:
            t += (alphabet_lst.index(alphabet) + 3)
print(t)