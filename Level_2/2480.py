dice_1, dice_2, dice_3 = map(int, input().split())

if dice_1 == dice_2 == dice_3:
    print(10000 + dice_1 * 1000)
elif dice_1 == dice_2 or dice_2 == dice_3:
    print(1000 + dice_2 * 100)
elif dice_3 == dice_1:
    print(1000 + dice_3 * 100)
else:
    print(max(dice_1, dice_2, dice_3) * 100)