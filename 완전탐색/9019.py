import sys
import collections


# Solution 1
def bfs(n: int) -> str:
    que = collections.deque([(n, '')])
    while que:
        n, path = que.popleft()
        if n == B:
            return path

        num = double(n)
        if num != n and num not in visited:
            que.append((num, path + 'D'))
            visited.add(num)

        num = substitute(n)
        if num != n and num not in visited:
            que.append((num, path + 'S'))
            visited.add(num)

        num = left(n)
        if num != n and num not in visited:
            que.append((num, path + 'L'))
            visited.add(num)

        num = right(n)
        if num != n and num not in visited:
            que.append((num, path + 'R'))
            visited.add(num)


def double(n: int) -> int:
    return (2 * n) % 10000


def substitute(n: int) -> int:
    n -= 1
    if n < 0:
        return 9999
    return n


def left(n: int) -> int:
    quotient, remainder = divmod(n, 1000)
    return remainder * 10 + quotient


def right(n: int) -> int:
    quotient, remainder = divmod(n, 10)
    return remainder * 1000 + quotient


T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())

    visited = set()
    print(bfs(A))


# Solution 2
def bfs(src: int, dst: int) -> str:
    que = collections.deque([(1, src), (-1, dst)])  # forward: 1 and backward: -1
    while que:
        ward, n = que.popleft()
        if ward == 1:
            if visited_backward[n]:
                return visited_forward[n] + visited_backward[n][::-1]

            num = double(1, n)
            if num != n and num not in visited_forward:
                que.append((1, num))
                visited_forward[num] = visited_forward[n] + 'D'

            num = substitute(1, n)
            if num != n and num not in visited_forward:
                que.append((1, num))
                visited_forward[num] = visited_forward[n] + 'S'

            num = left(1, n)
            if num != n and num not in visited_forward:
                que.append((1, num))
                visited_forward[num] = visited_forward[n] + 'L'

            num = right(1, n)
            if num != n and num not in visited_forward:
                que.append((1, num))
                visited_forward[num] = visited_forward[n] + 'R'

        elif ward == -1:
            if visited_forward[n]:
                return visited_forward[n] + visited_backward[n][::-1]

            if not n % 2:
                for num in double(-1, n):
                    if num != n and num not in visited_backward:
                        que.append((-1, num))
                        visited_backward[num] = visited_backward[n] + 'D'

            num = substitute(-1, n)
            if num != n and num not in visited_backward:
                que.append((-1, num))
                visited_backward[num] = visited_backward[n] + 'S'

            num = left(-1, n)
            if num != n and num not in visited_backward:
                que.append((-1, num))
                visited_backward[num] = visited_backward[n] + 'L'

            num = right(-1, n)
            if num != n and num not in visited_backward:
                que.append((-1, num))
                visited_backward[num] = visited_backward[n] + 'R'


def double(orientation: int, n: int):
    """
    only for the case when n is even.
    """
    if orientation == 1:
        return (2 * n) % 10000
    else:
        return n // 2, (n + 10000) // 2


def substitute(orientation: int, n: int) -> int:
    if orientation == 1:
        n -= 1
        if n < 0:
            return 9999
    else:
        n += 1
        if n > 9999:
            return 0
    return n


def left(orientation: int, n: int) -> int:
    if orientation == 1:
        quotient, remainder = divmod(n, 1000)
        return remainder * 10 + quotient
    else:
        quotient, remainder = divmod(n, 10)
        return remainder * 1000 + quotient


def right(orientation: int, n: int) -> int:
    if orientation == 1:
        quotient, remainder = divmod(n, 10)
        return remainder * 1000 + quotient
    else:
        quotient, remainder = divmod(n, 1000)
        return remainder * 10 + quotient


T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())

    # path dictionary
    visited_forward = collections.defaultdict(str)
    visited_backward = collections.defaultdict(str)
    print(bfs(A, B))
