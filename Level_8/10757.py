A, B = input().split()

lst = []
i = -1
ceiling = False
while i >= min(len(A), len(B)) * (-1):
    if ceiling:
        num = int(A[i]) + int(B[i]) + 1
    else:
        num = int(A[i]) + int(B[i])
    if num < 10:
        lst.append(num)
        ceiling = False
    else:
        lst.append(num - 10)
        ceiling = True
    i -= 1
if len(A) > len(B):
    while i >= len(A) * (-1):
        if ceiling:
            num = int(A[i]) + 1
        else:
            num = int(A[i])
        if num < 10:
            lst.append(num)
            ceiling = False
        else:
            lst.append(num - 10)
            ceiling = True
    i -= 1
else:
    while i >= len(B) * (-1):
        if ceiling:
            num = int(B[i]) + 1
        else:
            num = int(B[i])
        if num < 10:
            lst.append(num)
            ceiling = False
        else:
            lst.append(num - 10)
            ceiling = True
    i -= 1
if ceiling:
    lst.append(1)

lst.reverse()
for i in lst:
    print(i, end='')