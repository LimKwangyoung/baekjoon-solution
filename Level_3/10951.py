while True:
    try:
        A, B = map(int, input().split())
    except:
        break
    else:
        print(A + B)