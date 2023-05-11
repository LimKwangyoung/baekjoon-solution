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