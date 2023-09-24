import sys
from itertools import combinations


# Solution 1
def euclidean(num1: int, num2: int) -> int:
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return num2


t = int(sys.stdin.readline())
for _ in range(t):
    n, *lst = map(int, sys.stdin.readline().split())

    result = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            result += euclidean(lst[i], lst[j])
    print(result)


# Solution 2
def euclidean(num1: int, num2: int) -> int:
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return num2


t = int(sys.stdin.readline())
for _ in range(t):
    n, *lst = map(int, sys.stdin.readline().split())
    lst = combinations(lst, 2)

    result = 0
    for i, j in lst:
        result += euclidean(i, j)
    print(result)
