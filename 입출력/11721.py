import sys

word = sys.stdin.readline()

print('\n'.join(word[i:i + 10] for i in range(0, len(word), 10)))
