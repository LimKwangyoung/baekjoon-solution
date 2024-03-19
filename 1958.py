import sys

words = [sys.stdin.readline().strip() for _ in range(3)]

n1, n2, n3 = len(words[0]), len(words[1]), len(words[2])
dp = [[[0] * n1 for _ in range(n2)] for _ in range(n3)]

for i in range(n3):
    for j in range(n2):
        for k in range(n1):
            if words[0][k] == words[1][j] == words[2][i]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
print(dp)

"""
abcdefohijksdg
bdefgabsdg
efgdasdg
"""
"""
abcdefdsghijklmn
bdeafg
efg
"""