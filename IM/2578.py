import sys
import collections

coord = collections.defaultdict(tuple)
for i in range(5):
    for j, val in enumerate(sys.stdin.readline().split()):
        coord[val] = (i, j)

rows, cols = [0] * 5, [0] * 5
dia = rev_dia = 0

result = cnt = 0
for i in range(5):
    nums = sys.stdin.readline().split()
    if cnt >= 3:
        continue

    for j, val in enumerate(nums):
        if cnt >= 3:
            break
        r, c = coord[val]

        rows[r] += 1
        if rows[r] == 5:
            cnt += 1
        cols[c] += 1
        if cols[c] == 5:
            cnt += 1
        if r == c:
            dia += 1
            if dia == 5:
                cnt += 1
        if r + c == 4:
            rev_dia += 1
            if rev_dia == 5:
                cnt += 1

        if cnt >= 3:
            result = 5 * i + (j + 1)
print(result)
