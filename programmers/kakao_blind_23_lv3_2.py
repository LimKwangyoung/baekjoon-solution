def solution(numbers):
    result = []
    for num in numbers:
        binary = bin(num)[2:]

        height = 1
        while 2 ** height - 1 < len(binary):
            height += 1
        n = 2 ** height - 1
        binary = binary.zfill(n)

        stack = [(0, n - 1)]
        while stack:
            left, right = stack.pop()
            if left == right:
                continue

            mid = (left + right) // 2
            if binary[mid] == '0':
                left_child = (left + mid - 1) // 2
                right_child = (mid + 1 + right) // 2
                if binary[left_child] == '1' or binary[right_child] == '1':
                    result.append(0)
                    break
            stack.append((left, mid - 1))
            stack.append((mid + 1, right))
        else:
            result.append(1)
    return result
