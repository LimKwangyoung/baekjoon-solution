import sys
import collections


def hashing(lst: list[str]) -> str:
    return ''.join(lst)


N = int(sys.stdin.readline())
current = list(sys.stdin.readline().strip())
target = list(sys.stdin.readline().strip())

change = {'0': '1', '1': '0'}

visited_forward, visited_backward = set(), set()
visited_forward.add(hashing(current))
visited_backward.add(hashing(target))

que_forward, que_backward = collections.deque([current, 0]), collections.deque([target, 0])
while que_forward or que_backward:
    if que_forward:
        tmp, cnt = que_forward.popleft()


