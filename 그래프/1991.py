import sys
import collections


def preorder(node: str) -> None:
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node: str) -> None:
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])


def postorder(node: str) -> None:
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')


N = int(sys.stdin.readline())

tree = {}
for _ in range(N):
    parent, left, right = sys.stdin.readline().split()
    tree[parent] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
