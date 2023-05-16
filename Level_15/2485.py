import sys


def find_gcd(a: int, b: int) -> int:
    while a % b != 0:
        a, b = b, a % b
    return b


N = int(sys.stdin.readline())
tree_lst = list(map(int, sys.stdin.readlines()))
interval_lst = [tree_lst[i + 1] - tree_lst[i] for i in range(N - 1)]

gcd = interval_lst[0]
for i in range(1, N - 1):
    gcd = find_gcd(gcd, interval_lst[i])
print(sum(i // gcd - 1 for i in interval_lst))
