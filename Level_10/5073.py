while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if ((a >= b and a >= c) and (a >= b + c)) or ((b >= c and b >= a) and (b >= c + a)) or ((c >= a and c >= b) and (c >= a + b)):
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')
