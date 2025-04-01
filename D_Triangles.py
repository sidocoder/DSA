n = int(input())
arr = list(map(int, input().split()))

arr.sort()  # Sort the array

for i in range(n - 2): 
    if arr[i] + arr[i + 1] > arr[i + 2]: 
        print("YES")
        break
else:
    print("NO")  
