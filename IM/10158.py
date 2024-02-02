import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

dx = dy = True
for _ in range(t % (2 * w)):
    if dx:
        p += 1
    else:
        p -= 1
    if p == w:
        dx = False
    elif p == 0:
        dx = True

for _ in range(t % (2 * h)):
    if dy:
        q += 1
    else:
        q -= 1
    if q == h:
        dy = False
    elif q == 0:
        dy = True
print(p, q)
