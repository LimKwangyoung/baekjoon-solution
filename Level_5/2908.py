num_1, num_2 = input().split()

num_1 = int(num_1[-1] + num_1[1] + num_1[0])
num_2 = int(num_2[-1] + num_2[1] + num_2[0])
print(max(num_1, num_2))