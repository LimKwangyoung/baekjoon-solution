import sys

S = sys.stdin.readline().rstrip()

string = ''
for i in S:
    if i.isupper():
        string += chr(((ord(i) - 65) + 13) % 26 + 65)
    elif i.islower():
        string += chr(((ord(i) - 97) + 13) % 26 + 97)
    else:
        string += i
print(string)
