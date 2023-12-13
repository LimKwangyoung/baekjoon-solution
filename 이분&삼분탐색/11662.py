import math
import sys


# # Solution 1 (mathematical loop)
# def cal_distance(time: int) -> float:
#     minho = (Ax + (Bx - Ax) / interval * time, Ay + (By - Ay) / interval * time)
#     kangho = (Cx + (Dx - Cx) / interval * time, Cy + (Dy - Cy) / interval * time)
#
#     return math.sqrt((minho[0] - kangho[0])**2 + (minho[1] - kangho[1])**2)
#
#
# Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, sys.stdin.readline().split())
#
# interval = 1000000
# minimum = sys.maxsize
# for t in range(interval + 1):
#     minimum = min(minimum, cal_distance(t))
# print(minimum)

# # Solution 2 (derivative)
# def cal_distance(time: int) -> float:
#     return math.sqrt(((dx1 - dx2) / interval * time + (Ax - Cx))**2 + ((dy1 - dy2) / interval * time + (Ay - Cy))**2)
#
#
# Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, sys.stdin.readline().split())
#
# dx1, dy1 = Bx - Ax, By - Ay
# dx2, dy2 = Dx - Cx, Dy - Cy
# interval = 1000000
#
# if dx1 == dx2 and dy1 == dy2:
#     t = 0
# else:
#     t = (-1) * interval * ((dx1 - dx2) * (Ax - Cx) + (dy1 - dy2) * (Ay - Cy)) / ((dx1 - dx2)**2 + (dy1 - dy2)**2)
#
# if 0 <= t <= interval:
#     result = cal_distance(t)
# else:
#     result = min(cal_distance(0), cal_distance(interval))
# print(result)

# Solution 3 (ternary search)
