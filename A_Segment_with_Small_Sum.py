n, s = [int() for i in input().split()]
arr=[int(i) for i in input().split()]

left,right = 0,0
summ,longest = 0,0

while right < n:
    summ = sum(arr[left:right + 1])
    if summ > s:
        
        summ -= arr[left]
        left += 1
    else:
        longest = max(longest,right -left + 1)
        right += 1
print(longest) 
    
 

