import sys

# Solution 1 (stack)
T = int(sys.stdin.readline())


def vps(s: str) -> bool:
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            return False

    return not stack


for _ in range(T):
    string = sys.stdin.readline().rstrip()
    print('YES' if vps(string) else 'NO')

# Solution 2 (not stack)
T = int(sys.stdin.readline())

for _ in range(T):
    string = sys.stdin.readline().rstrip()
    while '()' in string:
        string = string.replace('()', '')
    print('YES' if not string else 'NO')
