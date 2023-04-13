word = input()

start, end = 0, len(word) - 1
while start < end:
    if word[start] != word[end]:
        print(0)
        break
    start += 1
    end -= 1
else:
    print(1)