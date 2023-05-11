import sys

N, M = map(int, sys.stdin.readline().split())

pocket_dict1, pocket_dict2 = {}, {}
for i in range(N):
    name = sys.stdin.readline().rstrip()
    pocket_dict1[name] = i + 1
    pocket_dict2[i + 1] = name

for _ in range(M):
    question = sys.stdin.readline().rstrip()
    if question.isalpha():
        print(pocket_dict1[question])
    else:
        print(pocket_dict2[int(question)])
