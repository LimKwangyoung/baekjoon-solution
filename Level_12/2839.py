# Solution 1
N = int(input())

bag_lst = []
for cnt_5kg in range(N // 5 + 1):
    cnt_3kg, remainder = divmod(N - 5 * cnt_5kg, 3)
    if remainder == 0:
        bag_lst.append(cnt_3kg + cnt_5kg)
print(min(bag_lst) if bag_lst else -1)

# Solution 2
N = int(input())

for cnt_3kg in range(N // 3 + 1):  # mathematically, calculating 3 kg first is faster than 5 kg.
    cnt_5kg, remainder = divmod(N - 3 * cnt_3kg, 5)
    if remainder == 0:
        print(cnt_3kg + cnt_5kg)
        break
else:
    print(-1)
