n ,k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for num in queries:
    target = num
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            print('YES')
            break
    else:
        print('NO')
