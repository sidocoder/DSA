t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    left = 0
    bracket_cnt = 0
    right = n - 1  

    while right >= 0:
        if s[right] == ')':
            bracket_cnt += 1
            right -= 1
        else:
            break
    
    characters = right - left + 1
    
    if characters < bracket_cnt:
        print('Yes')
    else:
        print('No')

