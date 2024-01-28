import sys
import collections

# Solution 1
S = sys.stdin.readline().rstrip()

alphabet_dict = collections.Counter(S)
for i in range(ord('a'), ord('z') + 1):
    print(alphabet_dict[chr(i)] if chr(i) in alphabet_dict else 0, end=' ')

# Solution 2
S = sys.stdin.readline().rstrip()

lst = [0] * 26
for i in S:
    lst[ord(i) - 97] += 1
print(*lst)
