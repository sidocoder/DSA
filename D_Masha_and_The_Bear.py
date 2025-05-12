n, k = map(int, input().split())
preferences = [tuple(map(int, input().split())) for _ in range(k)]


parent = [i for i in range(n + 1)]

matched = 0
for i in range(k):
    x, y = preferences[i]

   
    xr = x
    while parent[xr] != xr:
        parent[xr] = parent[parent[xr]]
        xr = parent[xr]

   
    yr = y
    while parent[yr] != yr:
        parent[yr] = parent[parent[yr]]
        yr = parent[yr]

    
    if xr != yr:
        parent[yr] = xr
        matched += 1

print(k - matched)

