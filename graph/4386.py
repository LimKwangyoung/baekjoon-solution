import sys
import heapq


def find(node: int) -> int:
    while node != parents[node]:
        node = parents[node]
    return node


def union(node_1: int, node_2: int) -> bool:
    root_1 = find(node_1)
    root_2 = find(node_2)
    if root_1 == root_2:
        return False
    parents[root_2] = root_1
    return True


def cal_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2), 2)


n = int(sys.stdin.readline())
stars = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]

distances = []
for i in range(n - 1):
    for j in range(i + 1, n):
        heapq.heappush(distances, (cal_distance(stars[i][0], stars[i][1], stars[j][0], stars[j][1]), i, j))

result = 0
cnt = 0
parents = [i for i in range(n)]
while distances:
    distance, vertex_1, vertex_2 = heapq.heappop(distances)
    ans = union(vertex_1, vertex_2)
    if ans:
        result += distance
        cnt += 1

    if cnt == n - 1:
        break
print(result)
