n= int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pref = [0]
for i in range(n):
    pref.append(pref[-1] + a[i] * b[i])
    
ans = pref[-1]

for i in range(n):
    # odd 
    l, r = i-1, i + 1
    prof = a[i] * b[i]
    while l > 0 and r < n:
        prof += a[r] * b[l]
        prof += a[l] * b[r]
        ans = max(ans, prof + (pref[-1] - pref[r + 1]) + pref[l])  
        r += 1
        l -= 1
    # even 
    prof = 0
    l, r = i, i + 1
    while l > 0 and r < n:
        prof += a[r] * b[l]
        prof += a[l] * b[r]
        ans = max(ans, prof + (pref[-1] - pref[r + 1]) + pref[l])
        l -= 1
        r += 1
print(ans)
        