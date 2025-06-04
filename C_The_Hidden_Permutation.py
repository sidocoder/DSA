t = int(input())
for _ in range(t):
    n = int(input())
    matrx = []
    for _ in range(n):
        matrx.append(list(map(int, list(input()))))

    permutation = [0] * n
    used_positions = [False] * n
    
    for val in range(n, 0, -1):
        s_val = 0
        for u in range(1, val):
            if matrx[val - 1][u - 1] == 1:
                s_val += 1
        
        target_idx = s_val
        count = -1
        
        for i in range(n):
            if not used_positions[i]:
                count += 1
            
            if count == target_idx:
                permutation[i] = val
                used_positions[i] = True
                break
    
    print(*(permutation))