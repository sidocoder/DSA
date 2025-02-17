x = int(input())
for i in range(x):
    y, z = map(int, input().split())
    res = []
    for j in range(y):
        mat = list(map(int, input().split()))
        res.append(mat)
    total = 0
    for k in range(y):
        for l in range(z):
            sum1 = 0
            m = k
            n = l
            while m < y and n < z:
                sum1+=res[m][n]
                m+=1
                n+=1
            m = k-1
            n = l-1
            while m >=0 and n>=0:
                sum1+=res[m][n]
                m-=1
                n-=1
            m = k-1
            n = l+1
            while m>=0 and n<z:
                sum1+=res[m][n]
                m-=1
                n+=1
            m = k+1
            n = l-1
            while n>=0 and m<y:
                sum1+=res[m][n]
                m+=1
                n-=1
            total = max(sum1, total)
    print(total)
            
