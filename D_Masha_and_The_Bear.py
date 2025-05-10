# from collections import defaultdict

# n, k = map(int, input().split())
# guests = []

# for _ in range(k):
#     x, y = map(int, input().split())
#     guests.append((x, y))

# snack = defaultdict(int)
# for x, y in guests:
#     snack[x] += 1
#     snack[y] += 1


# available = set(range(1, n + 1))

# sad_count = 0
# for x, y in guests:
#     if x in available or y in available:
       
#         if x in available:
#             available.remove(x)
#         elif y in available:
#             available.remove(y)
#     else:
        
#         sad_count += 1

# print(sad_count)

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

