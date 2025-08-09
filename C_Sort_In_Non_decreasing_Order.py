t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    p = set(int(x) - 1 for x in input().split())  # convert to 0-indexed

    if a == sorted(a):
        print('YES')
    else:
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                if i in p: 
                    continue
                else:
                    print('NO')
                    break
        else:
            print('YES')
