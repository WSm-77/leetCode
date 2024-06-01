class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs_visit(x, y):
            nonlocal visited, neighbours, R, C

            visited[x][y] = True

            for dx, dy in neighbours:
                newX, newY = x + dx, y + dy 
                if (0 <= newX < R) and (0 <= newY < C) and not visited[newX][newY] and int(grid[newX][newY]) == 1:
                    dfs_visit(newX, newY)


        R = len(grid)
        C = len(grid[0])
        visited = [[False for _ in range(C)] for _ in range(R)]
        neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        islandsCnt = 0

        for x in range(R):
            for y in range(C):
                if not visited[x][y] and int(grid[x][y]) == 1:
                    islandsCnt += 1
                    dfs_visit(x, y)
        
        return islandsCnt
    
if __name__ == "__main__":
    test = Solution()
    grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]
    print(test.numIslands(grid))
    grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]
    print(test.numIslands(grid))
    grid = [
            ["1"],
            ["1"]
            ]
    print(test.numIslands(grid))