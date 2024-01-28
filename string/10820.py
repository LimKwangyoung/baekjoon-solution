import sys

string_lst = sys.stdin.readlines()
for i in string_lst:
    i = i.rstrip('\n')

    lst = [0] * 4
    for j in i:
        if j.islower():
            lst[0] += 1
        elif j.isupper():
            lst[1] += 1
        elif j.isnumeric():
            lst[2] += 1
        else:
            lst[3] += 1
    print(*lst)
