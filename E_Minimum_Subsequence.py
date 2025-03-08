t = int(input())
for _ in range(t):
    n = int(input())
    nums = map(int, input().split())

    stack = []
    popped = []
    count = 0
    for num in nums:
        stack.append(num)
        if stack and num == stack[-1]:
            m = stack.pop()
            if 
            count += 1
        
    print(count + 1)
    print()

    