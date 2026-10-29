
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            # Stop if outside the grid or on water
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0"):
                return

            # Mark this land as visited
            grid[r][c] = "0"

            # Visit all four directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands

        