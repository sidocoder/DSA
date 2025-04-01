n = int(input())
arr = list(map(int, input().split()))

length = len(arr)
i = 0
while n > 0:
    n = n - arr[i % length]
    if n <= 0:
        print(i % length + 1)

    i += 1


