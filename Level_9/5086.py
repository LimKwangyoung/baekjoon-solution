while True:
    A, B = map(int, input().split())
    if A == B == 0:
        break
    if A < B and not B % A:
        print('factor')
    elif A > B and not A % B:
        print('multiple')
    else:
        print('neither')
