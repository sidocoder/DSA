from collections import deque

def bfs(grid, visited, i, j, n, m):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    volume = grid[i][j]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] > 0:
                visited[nx][ny] = True
                volume += grid[nx][ny]
                q.append((nx, ny))
    return volume

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    max_volume = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] > 0:
                lake_volume = bfs(grid, visited, i, j, n, m)
                max_volume = max(max_volume, lake_volume)

    print(max_volume)
