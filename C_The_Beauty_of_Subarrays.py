t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
   
      
    pos = [0] * (n + 1)
    for index in range(n):
        pos[arr[index]] = index
    
    
    min_pos = n
    max_pos = -1
    ans = []
    
    for m in range(1, n + 1):
        min_pos = min(min_pos, pos[m])
        max_pos = max(max_pos, pos[m])
        if max_pos - min_pos + 1 == m:
            ans.append('1')
        else:
            ans.append('0')
    
    print(''.join(ans))



