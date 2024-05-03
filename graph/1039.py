import sys

N, K = sys.stdin.readline().split()
nums = list(map(int, list(N)))
K = int(K)

if len(nums) == 1 or (len(nums) == 2 and sum(nums[1:]) == 0):
    print(-1)
else:
    result = float('-inf')
    que = [(nums, K)]
    for idx1 in range(len(nums) - 1):
        if not que:
            break
        new_que = que[:]
        for nums, K in que:
            indices = []
            maximum = float('-inf')
            for idx2 in range(idx1 + 1, len(nums)):
                if nums[idx2] > maximum:
                    maximum = nums[idx2]
                    indices = [idx2]
                elif nums[idx2] == maximum:
                    indices.append(idx2)

            for idx2 in indices:
                tmp = nums[:]
                tmp[idx1], tmp[idx2] = tmp[idx2], tmp[idx1]
                if K == 1:
                    n = len(tmp)
                    result = max(result, sum(tmp[i] * 10 ** (n - 1 - i) for i in range(n)))
                else:
                    new_que.append((tmp, K - 1))
        que = new_que
    for num, K in que:
        if K % 2:
            num[-1], num[-2] = num[-2], num[-1]
        result = max(result, sum(num[i] * 10 ** (len(num) - 1 - i) for i in range(len(num))))
    print(result)
