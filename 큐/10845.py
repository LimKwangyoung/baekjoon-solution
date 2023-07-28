import sys
import collections

N = int(sys.stdin.readline())

queue = collections.deque()
for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        print(0 if queue else 1)
    elif cmd[0] == 'front':
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)
