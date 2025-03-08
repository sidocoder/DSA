from collections import deque
n, k = map(int,input().split())
nums = map(int, input().split())

queue = deque()
for num in nums:
    if queue and len(queue) >= k:
        queue.pop()
    elif num in queue:
        continue
    else:
        queue.appendleft(num)
print(len(queue))
print(*queue)
    

