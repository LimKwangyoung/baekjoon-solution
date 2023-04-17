while True:
    n = int(input())
    if n == -1:
        break

    lst = []
    i = 1
    while i * i <= n:
        if not n % i:
            lst.append(i)
        i += 1
    for j in lst[::-1]:
        if j * j == n:
            continue
        lst.append(n // j)

    if n == sum(lst[:-1]):
        lst = map(str, lst[:-1])
        print(f'{n} = {" + ".join(lst)}')

    else:
        print(f'{n} is NOT perfect.')
