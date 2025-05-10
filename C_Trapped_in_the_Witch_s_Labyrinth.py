for _ in range(int(input())):
    n,m = map(int, input().split())
    grid = []
    for _ in range(n):
        s = input().split()
        grid.append(s)

    directions = {'R':(0,1), 'L':(0,-1), 'U':(1,0), 'D':(-1,0)}
    grid_out = [['']*m for _ in range(n)]

    for r,c in directions.items():
        
        
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'R':
                grid[i][j] = 'L'
            if grid[i][j] == "L":
                grid[i][j] = 'R'
            if grid[i][j] == "U":
                grid[i][j] = 'D'
            if grid[i][j] == "D":
                grid[i][j] = 'U'



def union(self, X, Y):
# Rank-based union
rootX = self.find(X)
rootY = self.find(Y)
if rootX != rootY:
rankX = self.rank[rootX]
rankY = self.rank[rootY]
if rankX > rankY:
self.root[rootY] = rootX
elif rankX < rankY:
self.root[rootX] = rootY
else:
self.root[rootY] = rootX
self.rank[rootX] += 1
