def splitgame(s):
    
    check_set = set(s)
    if len(check_set) == 1:
        return 2

    half = len(s) // 2
    div1 = s[:half]
    div2 = s[half:]
    
    set1 = set(div1)
    set2 = set(div2)
        
    return len(set1) + len(set2)



n = int(input())  
 
for i in range(n):
    length = int(input())
    s = input().strip()
    result = splitgame(s)
    print(result)
