import sys
import collections


def find_root(node: str) -> str:
    while node != roots[node][0]:
        node = roots[node][0]
    return node


T = int(sys.stdin.readline())

for _ in range(T):
    roots = collections.defaultdict(tuple)  # (root, level, number of child nodes)
    for _ in range(int(sys.stdin.readline())):
        friend_1, friend_2 = input().split()

        if roots[friend_1] and roots[friend_2]:
            root_1 = find_root(friend_1)
            root_2 = find_root(friend_2)
            if roots[root_1][1] > roots[root_2][1]:
                roots[root_1][2] += roots[root_2][2]
                roots[root_1][2] -= 1
                roots[root_2] = (root_1, 0, 0)
            else:
                if roots[root_1][1] == roots[root_2][1]:
                    roots[root_2][1] += 1
                roots[root_2][2] += roots[root_1][2]
                roots[root_2][2] -= 1
                roots[root_1] = (root_2, 0, 0)
        elif roots[friend_1]:
            root = find_root(friend_1)
            root[friend_2] = (root, 0, 0)
            roots[root][2] += 1
        elif roots[friend_2]:
            root = find_root(friend_2)
            root[friend_1] = (root, 0, 0)
            roots[root][2] += 1
        else:
            roots[friend_1] = roots[friend_2] = (friend_1, 2, 1)

        print(roots[find_root(friend_1)][2])
