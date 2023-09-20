import sys
import math

N, K = map(int, sys.stdin.readline().split())

max_height = math.ceil(math.log2(2 * N))  # max_height = 4
seg_tree = [0] * (2**max_height - 1)
result = []

# initialize a segment tree
def init(node: int) -> int:
    if node >= 2**(max_height - 1) - 1:
        if node < (2**(max_height - 1) - 1) + N:
            seg_tree[node] = 1
        return seg_tree[node]

    seg_tree[node] = init(2 * node + 1) + init(2 * node + 2)
    return seg_tree[node]


def update(node: int, idx: int, start: int, end: int):
    seg_tree[node] -= 1
    if start == end:
        result.append(start)
        seg_tree[node] = 0
        return

    mid = (start + end) // 2
    if idx <= mid:
        update(2 * node + 1, idx, start, mid)
    else:
        update(2 * node + 2, idx, mid + 1, end)


init(0)
i = 0
for _ in range(5):
    i = (i + K) % N
    update(0, i, 1, 2**(max_height - 1))  # update(0, 3, 1, 8)
print(seg_tree)
print(result)