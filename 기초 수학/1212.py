import sys

octal = sys.stdin.readline().rstrip()

print(bin(int(octal, 8))[2:])
