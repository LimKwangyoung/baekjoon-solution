# Solution 1
x_lst, y_lst = [], []

for _ in range(3):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
if x_lst.count(min(x_lst)) <= 1:
    x = min(x_lst)
else:
    x = max(x_lst)
if y_lst.count(min(y_lst)) <= 1:
    y = min(y_lst)
else:
    y = max(y_lst)
print(x, y)

# Solution 2
x_lst, y_lst = [], []

for _ in range(3):
    x, y = map(int, input().split())
    if x in x_lst:
        x_lst.remove(x)
    else:
        x_lst.append(x)
    if y in y_lst:
        y_lst.remove(y)
    else:
        y_lst.append(y)
print(x_lst[0], y_lst[0])  # faster than Solution 1
