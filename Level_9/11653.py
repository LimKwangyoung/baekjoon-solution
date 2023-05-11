# Solution 1
N = int(input())

num = 2
while num * num <= N:
    i = 2
    while i * i <= num:
        if not num % i:
            break
        i += 1
    else:  # case of prime number
        while not N % num:
            print(num)
            N //= num
        if N == 1:
            break
    num += 1
else:
    if N > 1:
        print(N)

# Solution 2
N = int(input())

num = 2
while N != 1:
    if not N % num:
        print(num)
        N //= num
    else:
        num += 1
