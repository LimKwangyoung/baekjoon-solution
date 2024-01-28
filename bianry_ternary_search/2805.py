import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(trees)
while start <= end:
    mid = (start + end) // 2
    # nums = sum(max(0, i - mid) for i in trees)
    nums = sum(i - mid for i in trees if i > mid)  # faster than max function

    if M <= nums:
        start = mid + 1
    else:
        end = mid - 1
print(end)
