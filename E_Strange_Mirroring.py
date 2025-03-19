from math import ceil
from math import log2
t = int(input())
for _ in range(t):
    s = input()
    q = int(input())
    n = len(s)
    queries = [int(x) for x in input().split()]
    def find(k):
        if 1<=k<=n:
            return s[k-1]
        
        curr_level = ceil(log2(ceil(k/n)))
        prev = 2**(curr_level - 1) * n
        k = k - prev 
        return find(k).swapcase()
    ans = []
    for query in queries :
        ans.append(find(query))
    print(*ans)