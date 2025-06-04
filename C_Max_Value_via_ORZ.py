t = int(input())
for _ in range(t):
    n,z = map(int, input().split())
    a = list(map(int, input().split()))

    _max = max(a)
    idx = a.index(_max)

    ans = max(a)
    for i in range(n):
        a[i] = a[i] | z
        z = a[i] & z
        a[idx] = 


    
 