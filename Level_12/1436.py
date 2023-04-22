# Solution 1
N = int(input())

title = 666
while N > 1:
    title += 1
    if '666' in str(title):
        N -= 1
print(title)

# Solution 2