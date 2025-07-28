
n = int(input())
a = list(map(int, input().split()))
 
pos_1 = a.index(1)
pos_n = a.index(n)
 
max_dist = 0
 
a[pos_1], a[0] = a[0], a[pos_1]
max_dist = max(max_dist, abs(a.index(1) - a.index(n)))
a[pos_1], a[0] = a[0], a[pos_1]  
 
a[pos_1], a[-1] = a[-1], a[pos_1]
max_dist = max(max_dist, abs(a.index(1) - a.index(n)))
a[pos_1], a[-1] = a[-1], a[pos_1]
 
a[pos_n], a[0] = a[0], a[pos_n]
max_dist = max(max_dist, abs(a.index(1) - a.index(n)))
a[pos_n], a[0] = a[0], a[pos_n]
 
a[pos_n], a[-1] = a[-1], a[pos_n]
max_dist = max(max_dist, abs(a.index(1) - a.index(n)))
a[pos_n], a[-1] = a[-1], a[pos_n]
 
print(max_dist)