import sys

N = int(sys.stdin.readline())
pillars = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

pillars.sort(key=lambda x: x[0])

result = 0
pl, pr = 0, N - 1
while pl < pr:
    left_height, right_height = pillars[pl][1], pillars[pr][1]

    if left_height < right_height:
        next = pl + 1
        while pillars[pl][1] > pillars[next][1]:
            next += 1
        result += (pillars[next][0] - pillars[pl][0]) * left_height
        pl = next
    else:
        next = pr - 1
        while pillars[pr][1] > pillars[next][1]:
            next -= 1
        result += (pillars[pr][0] - pillars[next][0]) * right_height
        pr = next
result += pillars[pl][1]
print(result)