import sys

N = int(sys.stdin.readline())

lst = []
for _ in range(N):
    name, korean, english, math = sys.stdin.readline().split()
    lst.append([name, int(korean), int(english), int(math)])
lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

print('\n'.join(i[0] for i in lst))
