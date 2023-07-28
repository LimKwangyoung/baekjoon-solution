import sys

cutting = sys.stdin.readline().rstrip()

while '()' in cutting:
    cutting = cutting.replace('()', '*')

stack = []
cnt = 0
for i in cutting:
    if i == '(':
        stack.append(i)
        cnt += 1
    elif i == ')':
        stack.pop()
    else:
        cnt += len(stack)
print(cnt)
