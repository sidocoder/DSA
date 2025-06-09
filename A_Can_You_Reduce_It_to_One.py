t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if 1 not in a:
        print("NO")
        continue

    reachable = [False] * n
    for i in range(n):
        if a[i] == 1:
            for j in range(i - k + 1, i + 1):
                if 0 <= j <= n - k:
                    for l in range(k):
                        reachable[j + l] = True

    if all(reachable[i] or a[i] == 1 for i in range(n)):
        print("YES")
    else:
        print("NO")
