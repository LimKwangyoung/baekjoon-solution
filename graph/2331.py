import sys
import collections

A, P = map(int, sys.stdin.readline().split())

lst = [A]
value = sum(int(i)**P for i in str(lst[-1]))
while value not in lst:
    lst.append(value)
    value = sum(int(i) ** P for i in str(lst[-1]))
print(lst.index(value))
