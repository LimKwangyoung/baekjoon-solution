import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    heights = sorted(list(map(int, sys.stdin.readline().split())))

    arr = [0] * N
    left, right = 0, N - 1
    for i in range(0, N, 2):
        arr[left] = heights[i]
        if i + 1 < N:
            arr[right] = heights[i + 1]

        left += 1
        right -= 1

    result = float('-inf')
    for i in range(N):
        result = max(result, abs(arr[(i + 1) % N] - arr[i]))
    print(result)
