from collections import defaultdict
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
   
    ans = []
    b.sort()
    sorted_a = sorted(a)
    
        
    for num in a:        
        index = sorted_a.index(num)
        ans.append(b[index])
        sorted_a[index] = None  
        
    print(*ans)