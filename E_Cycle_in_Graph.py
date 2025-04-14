from collections import defaultdict
import sys
sys.setrecursionlimit(200000)

n, m, k = map(int, input().split())
graph = defaultdict(list)


for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
parent = [-1] * (n + 1)
depth = [0] * (n + 1)
found_cycle = []

def dfs(node, par):
    visited[node] = True
    for neighbor in graph[node]:
        if neighbor == par:
            continue
        if visited[neighbor]:
            if depth[node] - depth[neighbor] + 1 >= k + 1:
                # Cycle of required length found
                cycle = []
                cur = node
                while cur != neighbor:
                    cycle.append(cur)
                    cur = parent[cur]
                cycle.append(neighbor)
                cycle.reverse()
                found_cycle.extend(cycle)
                return True
        else:
            parent[neighbor] = node
            depth[neighbor] = depth[node] + 1
            if dfs(neighbor, node):
                return True
    return False

# Start DFS from each unvisited node
for i in range(1, n + 1):
    if not visited[i]:
        if dfs(i, -1):
            break


print(len(found_cycle))
print(" ".join(map(str, found_cycle)))
