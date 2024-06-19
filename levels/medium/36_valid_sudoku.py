class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def validRowAndColl(board, rowAndColl) -> bool:
            inRow = [False for _ in range(9)]
            inColl = [False for _ in range(9)]

            for i in range(0, 9):
                currentRowSquare = board[rowAndColl][i]
                currentCollSquare = board[i][rowAndColl]
                if (currentRowSquare != "."):
                    currentRowSquare = int(currentRowSquare) - 1
                    if inRow[currentRowSquare]:
                        return False
                    else:
                        inRow[currentRowSquare] = True
                if (currentCollSquare != "."):
                    currentCollSquare = int(currentCollSquare) - 1
                    if inColl[currentCollSquare]:
                        return False
                    else:
                        inColl[currentCollSquare] = True
            
            return True
        
        def validSmallSquare(board, smallSquare) -> bool:
            inSmallSquare = [False for _ in range(9)]

            startRow = (smallSquare // 3) * 3
            startColl = (smallSquare % 3) * 3

            for R in range(startRow, startRow + 3):
                for C in range(startColl, startColl + 3):
                    currentSquare = board[R][C]
                    if currentSquare == ".":
                        continue

                    currentSquare = int(currentSquare) - 1
                    
                    if inSmallSquare[currentSquare]:
                        return False
                    else:
                        inSmallSquare[currentSquare] = True
            
            return True

        for i in range(9):
            if not validRowAndColl(board, i) or not validSmallSquare(board, i):
                return False
        
        return True 

if __name__ == "__main__":
    test = Solution()

    # board = \
    #     [["5","3",".",".","7",".",".",".","."]
    #     ,["6",".",".","1","9","5",".",".","."]
    #     ,[".","9","8",".",".",".",".","6","."]
    #     ,["8",".",".",".","6",".",".",".","3"]
    #     ,["4",".",".","8",".","3",".",".","1"]
    #     ,["7",".",".",".","2",".",".",".","6"]
    #     ,[".","6",".",".",".",".","2","8","."]
    #     ,[".",".",".","4","1","9",".",".","5"]
    #     ,[".",".",".",".","8",".",".","7","9"]]
    
    # print(test.isValidSudoku(board))

    # board = \
    #     [["8","3",".",".","7",".",".",".","."]
    #     ,["6",".",".","1","9","5",".",".","."]
    #     ,[".","9","8",".",".",".",".","6","."]
    #     ,["8",".",".",".","6",".",".",".","3"]
    #     ,["4",".",".","8",".","3",".",".","1"]
    #     ,["7",".",".",".","2",".",".",".","6"]
    #     ,[".","6",".",".",".",".","2","8","."]
    #     ,[".",".",".","4","1","9",".",".","5"]
    #     ,[".",".",".",".","8",".",".","7","9"]]

    # print(test.isValidSudoku(board))

    board = \
        [[".",".",".",  ".","5",".",    ".","1","."],
        [".","4",".",  "3",".",".",    ".",".","."],
        [".",".",".",  ".",".","3",    ".",".","1"],

        ["8",".",".",  ".",".",".",    ".","2","."],
        [".",".","2",  ".","7",".",    ".",".","."],
        [".","1","5",  ".",".",".",    ".",".","."],

        [".",".",".",  ".",".","2",    ".",".","."],
        [".","2",".",  "9",".",".",    ".",".","."],
        [".",".","4",  ".",".",".",    ".",".","."]]
    
    print(test.isValidSudoku(board))