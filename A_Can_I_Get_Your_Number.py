n = int(input())
strings = [input().strip() for _ in range(n)]

first = strings[0]
length = len(first)

prefix_count = 0
for i in range(length):
    current_char = first[i]
    for s in strings[1:]:
        if s[i] != current_char:
            print(prefix_count)
            exit()
    prefix_count += 1

print(prefix_count)
