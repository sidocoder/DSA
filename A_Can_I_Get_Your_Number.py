n = int(input())
strings = [input().strip() for _ in range(n)]

first = strings[0]
length = len(first)

count = 0
for i in range(length):
    current_char = first[i]
    for s in strings[1:]:
        if s[i] != current_char:
            print(count)
            exit()
    count += 1

print(count)
