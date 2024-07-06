import sys

N, B, W = map(int, sys.stdin.readline().split())
rocks = sys.stdin.readline().strip()

blacks = []  # indices of black stones
whites = [0] * N  # number of whites stones
for i in range(N):
    if rocks[i] == 'B':
        blacks.append(i)
    whites[i] += whites[i - 1] + (rocks[i] == 'W')

# just count the white stones
if not B:
    result = 0
    idx = 0
    while idx < N:
        if rocks[idx] == 'B':
            idx += 1
            continue

        cnt = 0
        while idx < N and rocks[idx] == 'W':
            idx += 1
            cnt += 1

        if cnt >= W:
            result = max(result, cnt)
# possible to all roads
elif len(blacks) <= B:
    result = N if whites[N - 1] >= W else 0
# focusing on black stones
else:
    result = 0
    blacks = [-1] + blacks + [N]
    for i in range(B + 1, len(blacks)):
        left = blacks[i - B - 1] + 1
        right = blacks[i] - 1
        tmp = whites[left - 1] if left else 0  # exception when left is 0
        if whites[right] - tmp >= W:
            result = max(result, right - left + 1)
print(result)
