import sys
import heapq
import bisect

# (선호도, 레벨)

N, M, K = map(int, sys.stdin.readline().split())
beers_1 = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]

# sort by level
beers_2 = sorted(beers_1, key=lambda x: (x[1], x[0]))

# print(beers_1)
# print(beers_2)

que = []
total = 0
for idx in range(N):
    heapq.heappush(que, beers_2[idx])
    total += beers_2[idx][0]

candidates = beers_2[N:]
preference_lst = list(map(lambda x: x[0], candidates))

flag = True
while total < M:
    preference, level = heapq.heappop(que)
    total -= preference

    candidates.append((preference, level))
    preference_lst.append(preference)

    candidates.sort(key=lambda x: (x[0], x[1]))
    preference_lst.sort()

    # print(candidates)
    # print(preference_lst)

    target = M - total
    # print(target)
    idx = bisect.bisect_left(preference_lst, target)

    if idx == len(preference_lst):
        flag = False
        break

    if preference_lst[idx] == preference:
        idx += 1

    if idx == len(preference_lst):
        flag = False
        break

    total += preference_lst[idx]
    heapq.heappush(que, candidates[idx])
    candidates = candidates[:idx] + candidates[idx + 1:]
    preference_lst = preference_lst[:idx] + preference_lst[idx + 1:]
if not flag:
    print(-1)
else:
    print(max(que, key=lambda x: x[1])[1])


"""
3 9 5
3 5
4 6
3 3
4 3
1 4
"""