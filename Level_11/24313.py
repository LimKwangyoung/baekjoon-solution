a_1, a_0 = map(int, input().split())
c = int(input())
n_0 = int(input())

if (a_1 == c and a_0 <= 0) or (a_1 < c and a_0 / (c - a_1) <= n_0):
    print(1)
else:
    print(0)
