class UnionFind:
    def __init__(self, size):
        self.root = list(range(size + 1))  

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

n = int(input())
p = list(map(int, input().split()))

uf = UnionFind(n)

for i in range(1, n + 1):
    uf.union(i, p[i - 1])

unique_trees = set()
for i in range(1, n + 1):
    unique_trees.add(uf.find(i))

print(len(unique_trees))
