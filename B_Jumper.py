for _ in range(int(input())):
    strg = input().strip()
    n = len(strg)

    if all(char == 'R' for char in strg):
        print(1)
    elif all(char == 'L' for char in strg):
        print(n + 1)       
    else:
        max_L = 0
        curr_L = 0        
        for char in strg:
            if char == 'L':
                curr_L += 1
                max_L = max(max_L, curr_L)
            else:
                curr_L = 0
       
        print(max_L + 1)