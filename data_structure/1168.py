import sys
import math

N, K = map(int, sys.stdin.readline().split())

max_height = math.ceil(math.log2(2 * N))
seg_tree = [0] * (2**max_height - 1)


# initialize a segment tree
def init(node: int) -> int:
    if node >= 2**(max_height - 1) - 1:
        if node < (2**(max_height - 1) - 1) + N:
            seg_tree[node] += 1
        return seg_tree[node]

    seg_tree[node] = init(2 * node + 1) + init(2 * node + 2)
    return seg_tree[node]


# delete and return the i-th element among remaining elements
def query(node: int, i: int, start: int, end: int) -> int:
    seg_tree[node] -= 1
    if start == end:
        return start

    mid = (start + end) // 2
    if i <= seg_tree[2 * node + 1]:
        return query(2 * node + 1, i, start, mid)
    else:
        return query(2 * node + 2, i - seg_tree[2 * node + 1], mid + 1, end)


result = []

init(0)
idx = 1
for n in range(N):
    idx += (K - 1)
    if idx % (N - n):
        idx %= (N - n)
    else:
        idx = (N - n)
    num = query(node=0, i=idx, start=1, end=2**(max_height - 1))
    result.append(str(num))
print('<' + ', '.join(result) + '>')
