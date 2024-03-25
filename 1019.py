import sys

# N = int(sys.stdin.readline())

result = [0] * 10
for i in range(1, 10):
    for s in str(i):
        result[int(s)] += 1
print(f'9 : {result}')

result = [0] * 10
for i in range(1, 100):
    for s in str(i):
        result[int(s)] += 1
print(f'99 : {result}')

result = [0] * 10
for i in range(1, 1000):
    for s in str(i):
        result[int(s)] += 1
print(f'999 : {result}')

result = [0] * 10
for i in range(1, 10000):
    for s in str(i):
        result[int(s)] += 1
print(f'9999 : {result}')

result = [0] * 10
for i in range(1, 20):
    for s in str(i):
        result[int(s)] += 1
print(f'19 : {result}')

result = [0] * 10
for i in range(1, 30):
    for s in str(i):
        result[int(s)] += 1
print(f'29 : {result}')

result = [0] * 10
for i in range(1, 7459):
    for s in str(i):
        result[int(s)] += 1
print(f'7458 : {result}')

result = [0] * 10
for i in range(1, 751):
    for s in str(i):
        result[int(s)] += 1
print(f'750 : {result}')

print(7*5*6+7*5*9+7*6*9)
print(7*5+7*6+7*9)
