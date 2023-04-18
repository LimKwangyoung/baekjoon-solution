"""
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
첫째 줄에 정수 N(1 <= N <= 10,000,000)이 주어진다.
N의 소인수분해 결과를 한 주에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

72      2\n2\n2\n3\n3
3       3
6       2\n3
2       2
9991    97\n103
"""
"""
숫자 2부터 시작하여 루트 N까지 소수를 탐색하며, 소수일 경우 N을 나눈다.
N을 소수로 나누었을 때 나머지가 0인 경우, 계속 나눌 수 있을 때까지 해당 소수로 나눈다.
더이상 해당 소수로 나눌 수 없을 경우, while 문을 다시 시작한다.
"""

# Solution 1
N = int(input())

num = 2
while num * num <= N:
    i = 2
    while i * i <= num:
        if not num % i:
            break
        i += 1
    else: # case of prime number
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
