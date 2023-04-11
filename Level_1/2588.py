num_1 = int(input())
num_2 = input()

num_3 = num_1 * int(num_2[-1])
num_4 = num_1 * int(num_2[1])
num_5 = num_1 * int(num_2[0])

print(num_3)
print(num_4)
print(num_5)
print(num_3 + num_4 * 10 + num_5 * 100)