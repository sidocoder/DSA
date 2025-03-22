from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    increments = defaultdict(int)
    
    for num in arr:
        remainder = num % k
        if remainder != 0:
            add = (k - remainder) % k
            increments[add] += 1
    
    max_moves = 0
    
    for add, count in increments.items():
        moves = (count - 1) * k + add + 1
        max_moves = max(max_moves, moves)
    
    print(max_moves)


