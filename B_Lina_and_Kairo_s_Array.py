t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    for i in range(n):
        if a[i] > a[(i + 1) % n]:
            count += 1

    print("Yes" if count <= 1 else "No")
