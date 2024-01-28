import sys

date_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
day_dict = {0: 'SUN', 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT'}

x, y = map(int, sys.stdin.readline().split())

days = 0
for month in range(1, x):
    days += date_dict[month]
days += y

print(day_dict[days % 7])
