n ,k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))


arr.sort()
for num in queries:
    target = num
    left = 0
    right = len(arr )- 1
    best = 0
   
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] <= target:
            best = mid + 1
            left = mid + 1
    print(best)
                



