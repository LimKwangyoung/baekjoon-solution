import sys

S = sys.stdin.readline().rstrip()

lst = []
for i in range(len(S)):
    lst.append(S[i:])
lst.sort()
print('\n'.join(lst))
