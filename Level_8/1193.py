X = int(input())

layer = 1
while (layer**2 - layer) / 2 + 1 <= X:
    layer += 1
layer -= 1

num = X - int(((layer**2 - layer) / 2 + 1))
if layer % 2:
    print(f'{layer - num}/{1 + num}')
else:
    print(f'{1 + num}/{layer - num}')