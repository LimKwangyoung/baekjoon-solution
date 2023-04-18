a, b, c = map(int, input().split())

if a >= b and a >= c:
    a = min(b + c - 1, a)
elif b >= c and b >= a:
    b = min(c + a - 1, b)
else:
    c = min(a + b - 1, c)
print(a + b + c)
