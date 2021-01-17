# 200. 岛屿数量
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。此外，你可以假设该网格的四条边均被水包围。
# 并查集解法
class UnionFind:
    def __init__(self, grid):
        row, col = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (row * col)
        self.rank = [0] * (row * col)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    self.parent[i * col + j] = i * col + j
                    self.count += 1

    def find_parent(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find_parent(x)
        rooty = self.find_parent(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]: #保证rootx最大，简化代码
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx #把rank 低的指向高的, 来合并
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1 # 合并后集合技术减一

    def get_count(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_row = len(grid)
        if grid_row == 0: return 0
        grid_col = len(grid[0])
        union_object = UnionFind(grid)
        for r in range(grid_row):
            for c in range(grid_col):
                if grid[r][c] == "1":
                    grid[r][c] = 0
                    for x, y in [(r - 1, c), (r+1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < grid_row and 0 <= y < grid_col and grid[x][y] == "1":
                            union_object.union(r * grid_col + c , x * grid_col + y)
        return union_object.get_count()



