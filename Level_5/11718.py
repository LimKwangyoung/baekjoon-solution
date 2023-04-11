"""
입력 받은 대로 출력하는 프로그램을 작성하시오.
입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다.
또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.
입력받은 그대로 출력한다.

Hello           Hello
Baekjoon        Baekjoon
Online Judge    Online Judge
"""

# Solution 1
while True:
    try:
        print(input())
    except EOFError: # cmd + D 를 의도적으로 입력
        break

# Solution 2
import sys

string_lst = sys.stdin.readlines() # cmd + D 를 의도적으로 입력
for i in string_lst:
    print(i[:-1])