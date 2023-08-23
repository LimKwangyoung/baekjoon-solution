import sys


# Solution 1(Doubly Linked List)
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Editor:
    def __init__(self):
        self.root = self.cur = Node()

    def set(self, s: str):
        for i in s:
            node = Node(i)
            self.cur.right, node.left = node, self.cur
            self.cur = self.cur.right

    def move_left(self):
        if self.cur is not self.root:
            self.cur = self.cur.left

    def move_right(self):
        if self.cur.right:
            self.cur = self.cur.right

    def delete(self):
        if self.cur is not self.root:
            if self.cur.right:
                next_node = self.cur.right
                self.cur = self.cur.left
                self.cur.right, next_node.left = next_node, self.cur
            else:
                self.cur = self.cur.left
                self.cur.right = None

    def insert(self, s: str):
        if self.cur.right:
            next_node = self.cur.right
            node = Node(s, self.cur, next_node)
            self.cur.right = next_node.left = node
        else:
            self.cur.right = Node(s, self.cur)
        self.cur = self.cur.right

    def result(self):
        self.root = self.root.right
        while self.root:
            print(self.root.val, end='')
            self.root = self.root.right


editor = Editor()
editor.set(sys.stdin.readline().rstrip())

for _ in range(int(sys.stdin.readline())):
    cmd, *string = sys.stdin.readline().split()
    if string:  # P(insert)
        editor.insert(string[0])
    elif cmd == 'L':  # L(move_left)
        editor.move_left()
    elif cmd == 'D':  # D(move_right)
        editor.move_right()
    else:  # B(delete)
        editor.delete()
editor.result()

# Solution 2(Stack)
stack_1, stack_2 = [], []  # it is faster than Solution 1.
for s in sys.stdin.readline().rstrip():
    stack_1.append(s)

for _ in range(int(sys.stdin.readline())):
    cmd, *string = sys.stdin.readline().split()
    if string:  # P
        stack_1.append(string[0])
    elif cmd == 'L' and stack_1:  # L
        stack_2.append(stack_1.pop())
    elif cmd == 'D' and stack_2:  # D
        stack_1.append(stack_2.pop())
    elif cmd == 'B' and stack_1:  # B
        stack_1.pop()
print(''.join((stack_1 + stack_2[::-1])))
