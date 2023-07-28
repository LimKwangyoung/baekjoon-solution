import sys
import collections

N = int(sys.stdin.readline())

queue = collections.deque()
for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push_front':
        queue.appendleft(int(cmd[1]))
    elif cmd[0] == 'push_back':
        queue.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        print(queue.popleft() if queue else -1)
    elif cmd[0] == 'pop_back':
        print(queue.pop() if queue else -1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        print(0 if queue else 1)
    elif cmd[0] == 'front':
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)
