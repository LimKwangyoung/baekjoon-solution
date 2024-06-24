import sys
import collections


def dfs(prev: str, level: int) -> None:
    global result

    if level == len(string):
        result += 1
        return

    for char in alphabets:
        if char != prev and alphabets[char] > 0:
            alphabets[char] -= 1
            dfs(prev=char, level=level + 1)
            alphabets[char] += 1


string = sys.stdin.readline().strip()

alphabets = collections.defaultdict(int)
for s in string:
    alphabets[s] += 1

result = 0
for s in alphabets:
    alphabets[s] -= 1
    dfs(prev=s, level=1)
    alphabets[s] += 1
print(result)
