from collections import deque
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or grid[0]:
            return 0
        islands = 0
        visited=set()
        for i in len(grid):
            for j in len(grid[i]):
                if grid[i][j] and (i,j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
        return islands
    def bfs(self, grid, i, j, visited):
        queue = deque ([(i,j)])
        visited.add((i,j))
        while queue:
            i,j