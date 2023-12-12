import math
import sys


# Solution 1 (mathematical loop)
def cal_distance(time: int) -> float:
    MinHo = (Ax + (Bx - Ax) / interval * time, Ay + (By - Ay) / interval * time)
    KangHo = (Cx + (Dx - Cx) / interval * time, Cy + (Dy - Cy) / interval * time)

    return math.sqrt((MinHo[0] - KangHo[0])**2 + (MinHo[1] - KangHo[1])**2)


Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, sys.stdin.readline().split())

interval = 1000000
minimum = sys.maxsize
for t in range(interval + 1):
    minimum = min(minimum, cal_distance(t))
print(minimum)

# Solution 2 (derivative)
