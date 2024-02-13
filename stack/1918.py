import sys

incoming = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
instack = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

stack = []
for token in sys.stdin.readline().strip():
    if token not in '+-*/()':
        print(token, end='')
    elif token == ')':
        while stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    elif not stack or token == '(' or incoming[token] > instack[stack[-1]]:
        stack.append(token)
    else:
        while stack and incoming[token] <= instack[stack[-1]]:
            print(stack.pop(), end='')
        stack.append(token)

while stack:
    print(stack.pop(), end='')
