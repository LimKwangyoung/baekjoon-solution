N, B = map(int, input().split())

lst = []
while True:
    quotient = N // B
    remainder = N % B
    lst.append(str(remainder)) if remainder <= 9 else lst.append(chr(remainder + 55))
    if quotient <= 0:
        break
    N = quotient

lst.reverse()
print(''.join(lst))