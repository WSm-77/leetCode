class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def dfs_visit(x, y):
            nonlocal rows, colls, neighbours

            # mark as visited
            grid[x][y] = -1

            area = 1
            for dx, dy in neighbours:
                newX, newY = x + dx, y + dy
                if (0 <= newX < rows) and (0 <= newY < colls) and grid[newX][newY] == 1:
                    area += dfs_visit(newX, newY)

            return area

        rows = len(grid)
        colls = len(grid[0])
        neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        maxArea = 0

        for x in range(rows):
            for y in range(colls):
                if grid[x][y] == 1:
                    maxArea = max(maxArea, dfs_visit(x, y))
        
        return maxArea
    
if __name__ == "__main__":
    test = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    
    print(test.maxAreaOfIsland(grid))
    
    grid = [[0,0,0,0,0,0,0,0]]
    print(test.maxAreaOfIsland(grid))