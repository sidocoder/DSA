
n = int(input())

for i in range(n):
    s = str(input())
    l = len(s)
    if l % 2 == 0:
        h = l // 2
        if s[:h] == s[h:]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')



    
   


