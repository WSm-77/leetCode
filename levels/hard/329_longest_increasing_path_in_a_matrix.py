class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        def max_path(row, coll):
            nonlocal matrix, pathLen, rows, colls

            if pathLen[row][coll] == None:
                pathLen[row][coll] = 1
                for x, y in directions:
                    nextRow = row + x
                    nextColl = coll + y
                    if 0 <= nextRow < rows and 0 <= nextColl < colls and matrix[row][coll] < matrix[nextRow][nextColl]:
                        pathLen[row][coll] = max(pathLen[row][coll], max_path(nextRow, nextColl) + 1)

            return pathLen[row][coll]
        # end def

        rows = len(matrix)
        colls = len(matrix[0])
        
        pathLen = [[None for _ in range(colls)] for _ in range(rows)]
        directions  = ((-1, 0), (0, -1), (1, 0), (0, 1))

        maxPath = 0
        for row in range(rows):
            for coll in range(colls):
                if pathLen[row][coll] == None:
                    maxPath = max(maxPath, max_path(row, coll))
        
        return maxPath
    
if __name__ == "__main__":
    test = Solution()
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    print(test.longestIncreasingPath(matrix))   # answer: 4
    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    print(test.longestIncreasingPath(matrix))   # answer: 4
    matrix = [[1]]
    print(test.longestIncreasingPath(matrix))   # answer: 1
