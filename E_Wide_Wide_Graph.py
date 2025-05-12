from collections import defaultdict
from bisect import bisect_left


import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    def dfs(node, depth, parent):
        dist[node] = depth
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs(neighbor, depth + 1, node)


    dist = [0] * n
    dfs(0, 0, -1)
    first = dist.index(max(dist))


    dist = [0] * n
    dfs(first, 0, -1)
    dist_first = dist[:]

    second = dist_first.index(max(dist_first))
    dist = [0] * n
    dfs(second, 0, -1)
    dist_second = dist[:]


    max_dist = [max(dist_first[i], dist_second[i]) for i in range(n)]
    max_dist.sort()


    res = []
    for k in range(1, n + 1):
        ind = bisect_left(max_dist, k)
        res.append(min(n, ind + 1))

    print(*res)
   
    pass
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
