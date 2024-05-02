def solution(dice):
    def mix(arr1: list, arr2: list) -> list:
        mix_result = []
        for x in arr1:
            for y in arr2:
                mix_result.append(x + y)
        return mix_result

    def match(arr1: list, arr2: list) -> int:
        win = 0
        length = len(arr1)
        for x in arr1:
            left, right = 0, length - 1
            while left <= right:
                mid = (left + right) // 2
                if arr2[mid] >= x:
                    right = mid - 1
                else:
                    left = mid + 1
            win += right + 1
        return win

    n = len(dice)
    prev = dict()
    for i, lst in enumerate(dice):
        prev[(i,)] = lst
    cur = prev

    cnt = 1
    while cnt < n // 2:
        cur = dict()
        for dices in prev.keys():
            for i in range(dices[-1] + 1, n):
                cur[dices + (i,)] = mix(prev[dices], dice[i])
        prev = cur
        cnt += 1

    for lst in cur:
        cur[lst].sort()

    result = 0
    maximum = float('-inf')
    for a in cur:
        b = tuple(set(range(n)) - set(a))
        w = match(cur[a], cur[b])
        if w > maximum:
            result = a
            maximum = w
    return list(map(lambda x: x + 1, result))
