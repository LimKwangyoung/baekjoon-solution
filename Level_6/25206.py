import sys

lst = sys.stdin.readlines()
grade_dict = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0': 2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

total = 0
credit_cnt = 0
for i in lst:
    _, credit, grade = i.split()
    if grade == 'P':
        continue
    else:
        total += float(credit) * grade_dict[grade]
        credit_cnt += float(credit)
print(total / credit_cnt)