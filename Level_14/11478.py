import sys

S = sys.stdin.readline().rstrip()

substring_set = set()
for i in range(1, len(S) + 1):
    for j in range(len(S) + 1 - i):
        substring_set.add(S[j:j + i])
print(len(substring_set))
