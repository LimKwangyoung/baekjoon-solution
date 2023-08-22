import sys

string_lst = sys.stdin.readlines()
for i in string_lst:
    print(len(i))

# for i in string_lst:
#     s = i[:-1]
#     lst = [0] * 4
#
#     for j in s:
#         if j.islower():
#             lst[0] += 1
#         elif j.isupper():
#             lst[1] += 1
#         elif j.isnumeric():
#             lst[2] += 1
#         else:
#             lst[3] += 1
#     print(*lst)
