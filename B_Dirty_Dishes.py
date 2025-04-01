n, bowl, plate = map(int, input().split())
arr = list(map(int, input().split()))

clean = 0
for num in arr:
    if num == 1:
        if bowl != 0:
            bowl -= 1
        else:
            clean += 1
    else:
        if plate != 0:
            plate -= 1
        elif bowl != 0:
            bowl -= 1
        else:
            clean += 1
print(clean)

   

