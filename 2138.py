import sys
import collections


def hashing(lst: list[str]) -> str:
    return ''.join(lst)


def bfs() -> int:
    visited_forward = dict()
    visited_forward[hashing(current)] = 0

    que_forward = collections.deque([current])
    while que_forward:
        cur = que_forward.popleft()
        cnt = visited_forward[hashing(cur)]

        # first setting
        cur[0] = change[cur[0]]
        cur[1] = change[cur[1]]
        if hashing(cur) == target:
            return cnt + 1
        elif hashing(cur) not in visited_forward:
            que_forward.append(cur[:])
            visited_forward[hashing(cur)] = cnt + 1

        if N >= 3:
            cur[2] = change[cur[2]]
            if hashing(cur) == target:
                return cnt + 1
            elif hashing(cur) not in visited_forward:
                que_forward.append(cur[:])
                visited_forward[hashing(cur)] = cnt + 1

        for i in range(N - 3):
            cur[i] = change[cur[i]]
            cur[i + 3] = change[cur[i + 3]]
            if hashing(cur) == target:
                return cnt + 1
            elif hashing(cur) not in visited_forward:
                que_forward.append(cur[:])
                visited_forward[hashing(cur)] = cnt + 1

        # last setting
        cur[N - 3] = change[cur[N - 3]]
        if hashing(cur) == target:
            return cnt + 1
        elif hashing(cur) not in visited_forward:
            que_forward.append(cur[:])
            visited_forward[hashing(cur)] = cnt + 1
    return -1


N = int(sys.stdin.readline())
current = list(sys.stdin.readline().strip())
target = sys.stdin.readline().strip()

change = {'0': '1', '1': '0'}
print(bfs())
