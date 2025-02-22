# from collections import Counter

# r, k, t = map(int, input().split())
# intervals = []
# for _ in range(t):
#     s, e = map(int, input().split())
#     intervals.append((s, e)) 

# queries = []
# for _ in range(t):
#     c, d = map(int, input().split())
#     queries.append((c, d))  

# hashh = Counter()
# for _ in range(r):
#     start = s
#     end = e
#     while start <= eend:
#         hashh[start] += 1
#         start+= 1


from collections import Counter

r, k, t = map(int, input().split())


intervals = []
for _ in range(t):
    s, e = map(int, input().split())
    intervals.append((s, e)) 


queries = []
for _ in range(t):
    c, d = map(int, input().split())
    queries.append((c, d))  


hashh = Counter()


for s, e in intervals:
    for num in range(s, e + 1):
        hashh[num] += 1

for c, d in queries:
    count = sum(1 for num in range(c, d + 1) if hashh[num] >= 2)
    print(count)  






