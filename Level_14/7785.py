import sys

n = int(sys.stdin.readline())

log_set = set()
for _ in range(n):
    name, log = sys.stdin.readline().split()
    if log == 'enter':
        log_set.add(name)
    else:
        log_set.remove(name)

print('\n'.join(sorted(log_set, reverse=True)))
