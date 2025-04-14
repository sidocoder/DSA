from collections import defaultdict
import sys

t = int(input())
for _ in range(t):
    n = int(input())
    tree = defaultdict(list)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    leaf_count = [0] * (n + 1)
    visited = [False] * (n + 1)

    def dfs(node, parent):
        visited[node] = True
        is_leaf = True
        count = 0
        for child in tree[node]:
            if not visited[child]:
                is_leaf = False
                count += dfs(child, node)
        if is_leaf:
            leaf_count[node] = 1
        else:
            leaf_count[node] = count
        return leaf_count[node]

    dfs(1, -1)

    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        print(leaf_count[x] * leaf_count[y])



