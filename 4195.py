import sys
<<<<<<< HEAD
import collections


def find_root(node: str) -> str:
    while node != roots[node][0]:
        node = roots[node][0]
    return node
=======
>>>>>>> 588f23e61f85c0886069bd102d5e4a7d1b40232f


T = int(sys.stdin.readline())

for _ in range(T):
<<<<<<< HEAD
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
=======
    F = int(sys.stdin.readline())

    sets = []
    for _ in range(F):
        friend_1, friend_2 = sys.stdin.readline().split()
        new_set = {friend_1, friend_2}

        if not sets:
            sets.append(new_set)
        else:
            for i in range(len(sets)):
                if new_set & sets[i]:
                    sets[i] = new_set | sets[i]
                    break
            else:
                sets.append(new_set)

        for i in range(len(sets)):
            for j in range(i + 1, len(sets)):
                if sets[i] & sets[j]:
                    sets[i] = sets[i] | sets[j]
                    sets[j] = None
                    break

        for i in sets:
            if friend_1 in i:
                print(len(i))
                break
>>>>>>> 588f23e61f85c0886069bd102d5e4a7d1b40232f
