import sys
import collections


def find_root(node: str) -> str:
    if roots[node] == node:
        return node

    roots[node] = find_root(roots[node])
    return roots[node]


def union(node_1: str, node_2: str) -> None:
    if node_1 == node_2:
        print(child[node_1])
        return
    if levels[node_1] < levels[node_2]:
        roots[node_1] = node_2
        child[node_2] += child[node_1]
        print(child[node_2])
    else:
        roots[node_2] = node_1
        if levels[node_1] == levels[node_2]:
            levels[node_1] += 1
        child[node_1] += child[node_2]
        print(child[node_1])


T = int(sys.stdin.readline())

for _ in range(T):
    roots = collections.defaultdict(str)
    levels = collections.defaultdict(int)
    child = collections.defaultdict(int)

    for _ in range(int(sys.stdin.readline())):
        friend_1, friend_2 = input().split()

        if roots[friend_1] and roots[friend_2]:
            root_1 = find_root(friend_1)
            root_2 = find_root(friend_2)
            union(root_1, root_2)
        elif roots[friend_1]:
            root = find_root(friend_1)
            roots[friend_2] = root
            child[root] += 1
            print(child[root])
        elif roots[friend_2]:
            root = find_root(friend_2)
            roots[friend_1] = root
            child[root] += 1
            print(child[root])
        else:
            roots[friend_1] = roots[friend_2] = friend_1
            levels[friend_1] = child[friend_1] = 2
            print(2)
