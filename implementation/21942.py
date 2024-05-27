import sys
import collections

months = {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151,
          7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334}

N, L, F = sys.stdin.readline().strip().split()

days, info = L.split('/')
hours, minutes = info.split(':')

N = int(N)
L = int(days) * 24 * 60 + int(hours) * 60 + int(minutes)
F = int(F)

lend = collections.defaultdict(dict)  # {part: {member, time}}
members = collections.defaultdict(int)
for _ in range(N):
    date, time, P, M = sys.stdin.readline().strip().split()

    cur = 0
    _, month, day = map(int, date.split('-'))
    cur += (months[month] + day - 1) * 24 * 60
    hour, minute = map(int, time.split(':'))
    cur += hour * 60 + minute

    # lend
    if not (P in lend and M in lend[P]):
        lend[P].update({M: cur})
    # return
    else:
        prev = lend[P][M]
        if L < cur - prev:
            members[M] += (cur - prev - L) * F
        del lend[P][M]
        if not lend[P]:
            del lend[P]

if members:
    for member in sorted(members.keys()):
        print(member, members[member])
else:
    print(-1)
