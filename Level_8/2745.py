N, B = input().split()

result = 0
for i in range(len(N)):
    try:
        value = int(N[i]) * int(B)**(len(N) - i - 1)
    except ValueError:
        value = (ord(N[i]) - 55) * int(B)**(len(N) - i - 1)
    result += value
print(result)
