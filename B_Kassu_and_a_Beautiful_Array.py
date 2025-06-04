t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    min_odd = float('inf')
    has_odd = False
    has_even = False

    for x in a:
        if x % 2 == 0:
            has_even = True
        else:
            has_odd = True
            if x < min_odd:
                min_odd = x

    if not has_odd:
        print("YES")
    elif not has_even:
        print("YES")
    else:
        possible_all_odd = True
        for x in a:
            if x % 2 == 0:
                if x <= min_odd:
                    possible_all_odd = False
                    break
        
        if possible_all_odd:
            print("YES")
        else:
            print("NO")