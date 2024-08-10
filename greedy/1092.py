import sys


def find_index(target: int) -> int:
    minimum = float('inf')
    minimum_index = 0
    for idx in range(N):
        if cranes[idx] < target:
            break
        if used[idx] < minimum:
            minimum = used[idx]
            minimum_index = idx
    return minimum_index


N = int(sys.stdin.readline())
cranes = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
M = int(sys.stdin.readline())
boxes = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
else:
    used = [0] * N
    for box in boxes:
        used[find_index(box)] += 1
    print(max(used))
