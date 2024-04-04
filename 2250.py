import sys
import collections


def inorder(node: str, level: int):
    global col

    if node == '-1':
        return

    inorder(graph[node][0], level + 1)
    width[level].append(col)
    col += 1
    inorder(graph[node][1], level + 1)


N = int(sys.stdin.readline())

root = None
graph = dict()
for _ in range(N):
    parent, *child = sys.stdin.readline().split()
    graph[parent] = child
    if not root:
        root = parent

col = 1
width = collections.defaultdict(list)
inorder(root, 1)

max_level, maximum = 0, float('-inf')
for i in sorted(width):
    num = max(width[i]) - min(width[i]) + 1
    if num > maximum:
        max_level = i
        maximum = num
print(max_level, maximum)