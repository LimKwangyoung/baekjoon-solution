import sys
import collections


def inorder(node: str, level: int) -> None:
    global col

    if graph[node][0] != '-1':
        inorder(graph[node][0], level + 1)
    width[level].append(col)
    col += 1
    if graph[node][1] != '-1':
        inorder(graph[node][1], level + 1)


N = int(sys.stdin.readline())

roots = [True] * (N + 1)
graph = dict()
for _ in range(N):
    parent, *child = sys.stdin.readline().split()
    graph[parent] = child
    for i in child:
        roots[int(i)] = False

for i in range(1, N + 1):
    if roots[i]:
        root = str(i)
        break

col = 1
width = collections.defaultdict(list)
inorder(root, 1)

max_level, maximum = 0, float('-inf')
i = 1
while width[i]:
    num = max(width[i]) - min(width[i]) + 1
    if num > maximum:
        max_level = i
        maximum = num
    i += 1
print(max_level, maximum)
