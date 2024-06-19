from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:            
        rows = len(heights)
        colls = len(heights[0])
        if rows == colls == 1:
            return [[0,0]]

        toCheck = deque()

        # check pacific ocean
        visited = [[False for _ in range(colls)] for _ in range(rows)]
        pacific = [[False for _ in range(colls)] for _ in range(rows)]
        for row in range(rows):
            toCheck.append((row, 0))
            visited[row][0] = True
            pacific[row][0] = True

        for coll in range(1, colls):
            toCheck.append((0, coll))
            visited[0][coll] = True
            pacific[0][coll] = True

        Solution.bfs(toCheck, pacific, heights, visited)

        # check atlantic ocean
        visited = [[False for _ in range(colls)] for _ in range(rows)]
        atlantic = [[False for _ in range(colls)] for _ in range(rows)]
        for row in range(rows):
            toCheck.append((row, colls - 1))
            visited[row][colls - 1] = True
            atlantic[row][colls - 1] = True

        for coll in range(colls - 1):
            toCheck.append((rows - 1, coll))
            visited[rows - 1][coll] = True 
            atlantic[rows - 1][coll] = True

        Solution.bfs(toCheck, atlantic, heights, visited)
        
        result = []
        for R in range(rows):
            for C in range(colls):
                if pacific[R][C] and atlantic[R][C]:
                    result.append([R, C])

        return result
    
    @staticmethod
    def bfs(queue: deque, ocean, heights, visited):
        rows = len(heights)
        colls = len(heights[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while queue:
            row, coll = queue.popleft()

            for x, y in directions:
                newRow = row + x
                newColl = coll + y
                if not (0 <= newRow < rows and 0 <= newColl < colls):
                    continue

                if not visited[newRow][newColl] and heights[newRow][newColl] >= heights[row][coll]:
                    ocean[newRow][newColl] = ocean[newRow][newColl] or ocean[row][coll]
                    visited[newRow][newColl] = True
                    queue.append((newRow, newColl))
    
if __name__ == "__main__":
    test = Solution()
    heights = [[1]]
    print(test.pacificAtlantic(heights))

    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(test.pacificAtlantic(heights))
    
    heights = [[10,10,10],[10,1,10],[10,10,10]]
    print(test.pacificAtlantic(heights))