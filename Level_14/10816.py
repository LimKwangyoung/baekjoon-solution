import sys

N = int(sys.stdin.readline())
num_dict = {}
for i in sys.stdin.readline().split():
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

M = int(sys.stdin.readline())
print(' '.join(str(num_dict[i]) if i in num_dict else '0' for i in sys.stdin.readline().split()))
