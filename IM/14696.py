import sys


def label(arr: list) -> list:
    result = [0] * 4
    for n in arr:
        result[4 - n] += 1
    return result


N = int(sys.stdin.readline())

for _ in range(N):
    a, *a_lst = map(int, sys.stdin.readline().split())
    b, *b_lst = map(int, sys.stdin.readline().split())

    a_label = label(a_lst)
    b_label = label(b_lst)

    for i in range(4):
        if a_label[i] > b_label[i]:
            print('A')
            break
        elif a_label[i] < b_label[i]:
            print('B')
            break
    else:
        print('D')
