t = int(input())
for i in range(t):
    n = int(input())
    strg = input().strip()
    arr = []

    x,y = 0, 0
    directions = [[(1,0)], [(0,-1)], [(-1,0)], [(0,1)]]  # right, down, left, up
    for i in range(n):
        if strg[i] == 'R':
            for r,c in directions[0]:
                nx ,ny = x + r, y + c
                x = nx
                y= ny
               
        elif strg[i] == 'D':
            for r,c in directions[1]:
                nx ,ny = x + r, y + c
                x = nx
                y= ny
             
        elif strg[i] == "L":
            for r,c in directions[2]:
                nx ,ny = x + r, y + c
                x = nx
                y= ny
                
        else:
            for r,c in directions[3]:
                nx ,ny = x + r, y + c
                x = nx
                y= ny
        arr.append((nx,ny))

    for r,c in arr:
        if r == 1 and c == 1:
            print('YES')
            break
    else:
        print('NO')

             

             



