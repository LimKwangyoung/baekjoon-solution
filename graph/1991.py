import sys


# Solution 1(Recursion)
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


# # Solution 2(Stack)
# def preorder() -> list[str]:
#     result = []
#     stack = ['A']
#     while stack:
#         node = stack.pop()
#         if node != '.':
#             result.append(str(node))
#             stack.append(tree[node][1])
#             stack.append(tree[node][0])
#     return result
#
#
# def inorder() -> list[str]:
#     result = []
#     stack = ['A']
#     while stack:
#         node = stack.pop()
#         if node != '.':
#             while node != '.':
#                 stack.append(node)
#                 node = tree[node][0]
#
#         if not stack:
#             break
#         node = stack.pop()
#         result.append(str(node))
#         stack.append(tree[node][1])
#     return result
#
#
# def postorder() -> list[str]:
#     result = []
#     stack = ['A']
#     while stack:
#         node = stack.pop()
#         if node != '.':
#             while node != '.':
#                 stack.append(node)
#                 node = tree[node][0]
#
#         node = stack.pop()
#         if node != tree[stack[-1]][1]:
#             result.append(str(node))
#             stack.append(tree[stack[-1]][1])
#         else:
#             stack.append(node)
#             stack.append(tree[node][1])
#
#
# N = int(sys.stdin.readline())
#
# tree = {}
# for _ in range(N):
#     parent, left, right = sys.stdin.readline().split()
#     tree[parent] = [left, right]

# print(''.join(preorder()))
# print(''.join(inorder()))
# print(postorder())
