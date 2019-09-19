from collections import deque


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        while grid is None:
            return 0

        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] and (i, j) not in visited):
                    self.bfs(grid, i, j, visited)
                    islands = islands + 1
        return islands

    def bfs(self, grid, i, j, visited):
        queue = deque([(i, j)])
        visited.add((i, j))
        while queue:
            i, j = queue.popleft()
            for move_i, move_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_i = i + move_i
                next_j = j + move_j
                if self.check_valid(grid, next_i, next_j, visited):
                    queue.append((next_i, next_j))
                    visited.add((next_i, next_j))

    def check_valid(self, grid, new_i, new_j, visited):
        limit_i, limit_j = len(grid), len(grid[0])
        if not (0 <= new_i < limit_i and 0 <= new_j < limit_j):
            return False
        if (new_i, new_j) in visited:
            return False
        return grid[new_i][new_j]

