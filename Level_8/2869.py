A, B, V = map(int, input().split())

day = 0
snail = 0
while True:
    day += 1
    snail += A
    if snail >= V:
        break
    snail -= B
print(day)