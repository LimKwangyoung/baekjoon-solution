matrix = [[] for _ in range(15)]

for i in range(5):
    word = input()
    for j in range(len(word)):
        matrix[j].append(word[j])

for i in matrix:
    if not i:
        break
    for j in i:
        print(j, end='')