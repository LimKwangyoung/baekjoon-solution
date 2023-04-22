N = int(input())

bag_lst = []
for cnt_5kg in range(N // 5 + 1):
    cnt_3kg, remainder = divmod(N - 5 * cnt_5kg, 3)
    if remainder == 0:
        bag_lst.append(cnt_3kg + cnt_5kg)
print(min(bag_lst) if bag_lst else -1)
