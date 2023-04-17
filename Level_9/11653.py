N = int(input())

while N != 1:
    start = 2
    for num in range(start, N + 1):
        i = 2
        while i * i <= num:
            if not num % i:
                break
            i += 1
        else:
            if not N % num:
                print(num)
                N //= num
                break
            else:
                start = num + 1
