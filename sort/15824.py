import sys

# Solution 1
N = int(sys.stdin.readline())
scales = sorted(list(map(int, sys.stdin.readline().split())))

exp = [1] * N
for i in range(1, N):
    exp[i] = exp[i - 1] * 2
    exp[i] %= 1000000007

result = 0
for i in range(N):
    result += scales[i] * (exp[i] - exp[N - i - 1])
    result %= 1000000007
print(result)

# Solution 2 (faster than Solution 1)
N = int(sys.stdin.readline())
scales = sorted(list(map(int, sys.stdin.readline().split())))

result = 0
exponential = 1
for i in range(N):
    result += exponential * (scales[i] - scales[N - 1 - i])
    result %= 1000000007
    exponential *= 2
    exponential %= 1000000007
print(result)
