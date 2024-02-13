import sys


T = int(sys.stdin.readline())

for _ in range(T):
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
