import sys

N = sys.stdin.readline().strip()
M = int(sys.stdin.readline())
breaks = set(map(int, sys.stdin.readline().split()))

cur = 100
approx_1 = ''
approx_2 = ''
for i in range(len(N)):
    if int(N[i]) not in breaks:
        approx_1 += N[i]
        approx_2 += N[i]
    else:
        n_1 = n_2 = int(N[i])

        # minimum
        while n_1 in breaks:
            n_1 -= 1
        approx_1 += str(n_1) * (len(N) - i)

        # maximum
        while n_2 in breaks:
            n_2 += 1
        approx_2 += str(n_2) * (len(N) - i)

        break

print(min(abs(100 - int(N)), int(N) - int(approx_1), int(approx_2) - int(N)))

