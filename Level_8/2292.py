N = int(input())

layer = 1
if N == 1:
    print(layer)
else:
    while (3 * layer**2 - 9 * layer + 8) <= N:
        layer += 1
    print(layer - 1)
