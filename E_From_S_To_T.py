
from collections import Counter

def transform(s, t, p):
    it = iter(t)
    for c in it:
        for c in s:
            if s == t:
                print('No')
    
    count_s = Counter(s)
    count_t = Counter(t)
    count_p = Counter(p)
    
    for c in count_t:
        if count_t[c] > count_s.get(c, 0) + count_p.get(c, 0):
            return "NO"
    
    return "YES"

q = int(input().strip())
results = []
for _ in range(q):
    s = input().strip()
    t = input().strip()
    p = input().strip()
    results.append(transform(s, t, p))

print((results))