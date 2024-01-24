import sys


# Solution 1
def dfs(a: int, b: int, c: int) -> None:
    if a == 0:
        result.add(c)

    if (a, b, c) not in visited:
        visited.add((a, b, c))
        if a != 0:
            dfs(a - min(a, B - b), b + min(a, B - b), c)  # from A to B
            dfs(a - min(a, C - c), b, c + min(a, C - c))  # from A to C
        if b != 0:
            dfs(a + min(b, A - a), b - min(b, A - a), c)  # from B to A
            dfs(a, b - min(b, C - c), c + min(b, C - c))  # from B to C
        if c != 0:
            dfs(a + min(c, A - a), b, c - min(c, A - a))  # from C to A
            dfs(a, b + min(c, B - b), c - min(c, B - b))  # from C to B


A, B, C = map(int, sys.stdin.readline().split())

result = set()
visited = set()
dfs(0, 0, C)
print(' '.join(map(str, sorted(result))))


# Solution 2
def dfs(a: int, b: int, c: int) -> None:
    stack = [(a, b, c)]
    while stack:
        a, b, c = stack.pop()
        if a == 0:
            result.add(c)
        if (a, b, c) not in visited:
            visited.add((a, b, c))
            if a != 0:
                stack.append((a - min(a, B - b), b + min(a, B - b), c))  # from A to B
                stack.append((a - min(a, C - c), b, c + min(a, C - c)))  # from A to C
            if b != 0:
                stack.append((a + min(b, A - a), b - min(b, A - a), c))  # from B to A
                stack.append((a, b - min(b, C - c), c + min(b, C - c)))  # from B to C
            if c != 0:
                stack.append((a + min(c, A - a), b, c - min(c, A - a)))  # from C to A
                stack.append((a, b + min(c, B - b), c - min(c, B - b)))  # from C to B


A, B, C = map(int, sys.stdin.readline().split())

result = set()
visited = set()
dfs(0, 0, C)
print(' '.join(map(str, sorted(result))))
