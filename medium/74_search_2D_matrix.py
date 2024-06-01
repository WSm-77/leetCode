class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        colls = len(matrix[0])

        beg = 0
        end = rows - 1

        while beg <= end:
            mid = (beg + end) // 2
            if matrix[mid][0] < target:
                beg = mid + 1
            else:
                end = mid - 1
        
        row = beg

        if row < rows and matrix[row][0] == target:
            return True
        
        row -= 1

        beg = 0
        end = colls - 1

        while beg <= end:
            mid = (beg + end) // 2
            if matrix[row][mid] < target:
                beg = mid + 1
            else:
                end = mid - 1
        
        coll = beg

        return coll < colls and matrix[row][coll] == target
    
if __name__ == "__main__":
    testTab = [[1,3,5,7],
               [10,11,16,20],
               [23,30,34,60]]
    
    test = Solution()

    print(test.searchMatrix(testTab, 3))
    print(test.searchMatrix(testTab, 4))
    print(test.searchMatrix(testTab, 23))
    print(test.searchMatrix(testTab, 60))

    testTab = [[1]]
    print(test.searchMatrix(testTab, 2))
        
