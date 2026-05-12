from collections import deque
#最伟大的BFS
def get_neighbors(x, y):
    # 上下左右四个方向
    s = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(x + dx, y + dy) for dx, dy in s]

def bfs(grid):
    if not grid or not grid[0]:
        return 0
    num = 0
    grid_shu = len(grid)      # 行数
    grid_heng = len(grid[0])  # 列数
    
    # 用for循环遍历，比while更清晰安全
    for i in range(grid_shu):
        for j in range(grid_heng):
            if grid[i][j] == 1:
                # 发现一个未访问的1，开始BFS
                grid[i][j] = -1  # 标记为已访问
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for neighbor in get_neighbors(x, y):
                        nx, ny = neighbor
                        # 修正后的边界条件
                        if 0 <= nx < grid_shu and 0 <= ny < grid_heng and grid[nx][ny] == 1:
                            grid[nx][ny] = -1
                            q.append((nx, ny))
                num += 1
    return num

grid = [
    [1,1,0,0,0,0],
    [1,1,0,0,0,0],
    [1,1,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

print("连通分量的数量: ", bfs(grid))