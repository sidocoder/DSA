from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False  # cycle found
        self.parent[rootY] = rootX
        return True

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        edges = []
        for _ in range(m):
            u, v, w = map(int, input().split())
            edges.append((w, u, v))

        edges.sort(reverse=True)  # sort edges by descending weight

        uf = UnionFind(n)
        graph = defaultdict(list)
        found = False

        for w, u, v in edges:
            if not uf.union(u, v):
                # Cycle detected on adding edge (u, v) with weight w
                # Track this as candidate with minimal weight edge w in that cycle
                print(w, 3)
                print(u, v, u)
                found = True
                break

        # The problem guarantees at least one cycle
        if not found:
            print("No cycle found (should not happen with valid input)")

# Run the function
solve()
