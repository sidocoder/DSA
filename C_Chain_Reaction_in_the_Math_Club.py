from collections import defaultdict
from collections import deque
n,m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
while True:
    remove = []
    for i in range(1, n + 1):
        if len(graph[i]) == 1:
            remove.append(i)
    
    if not remove:
        break  

    for student in remove:
        if graph[student]:  
            neighbor = graph[student].pop()  
            graph[neighbor].remove(student)  

    count += 1  

print(count)


    