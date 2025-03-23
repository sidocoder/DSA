from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, 0
count = 0

while l <= r and r < len(a):
    _max = max(a[l:r + 1])
    _min = min(a[l:r + 1])
    if _max - _min <= k:
        count += 1
        r += 1
    else:
        l += 1
        r = l

print(count)
