T = int(input())

for _ in range(T):
    C = int(input())
    quarter, dime, nickel, penny = 0, 0, 0, 0

    if C >= 25:
        quarter = C // 25
        C %= 25
    if C >= 10:
        dime = C // 10
        C %= 10
    if C >= 5:
        nickel = C // 5
        C %= 5
    penny = C
    print(quarter, dime, nickel, penny)
