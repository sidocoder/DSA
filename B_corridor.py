t = int(input())
for _ in range(t):
    n = int(input())
    traps = {}
    for _ in range(n):
        d, s = map(int, input().split())
        if d not in traps:
            traps[d] = s
        else:
            traps[d] = min(traps[d], s)
    k = 1
    while True:
        safe = True
        for d, s in traps.items():
            if d <= k:
                if 2 * (k - d) >= s:
                    safe = False
                    break
        if not safe:
            print(k - 1)
            break
        k += 1
