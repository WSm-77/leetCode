# from collections import deque

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:

        ####################
        # helper functions #
        ####################

        def emptySquares(board: list[list[str]]) -> list:
            stack_of_empty = []

            for R in range(9):
                for C in range(9):
                    if board[R][C] == ".":
                        stack_of_empty.append((R, C))

            return stack_of_empty
        
        def possibleNumbers(board: list[list[str]], row, coll) -> list:
            candidates = [True for _ in range(9)]

            #checking row
            for C in range(9):
                if board[row][C] != ".":
                    candidates[int(board[row][C]) - 1] = False

            #checking coll
            for R in range(9):
                if board[R][coll] != ".":
                    candidates[int(board[R][coll]) - 1] = False
            
            #checking small square
            start_row = (row // 3) * 3
            start_coll = (coll // 3) * 3
            for R in range(start_row, start_row + 3):
                for C in range(start_coll, start_coll + 3):
                    if board[R][C] != ".":
                        candidates[int(board[R][C]) - 1] = False
            
            return [i + 1 for i in range(9) if candidates[i]]
        
        def solveRek(board, empty_squares, index = 0):
            nonlocal solved
            # printBoard(board)
            if index == len(empty_squares):
                solved = True
                return

            row, coll = empty_squares[index]
            possible_numbers = possibleNumbers(board, row, coll)

            for number in possible_numbers:
                board[row][coll] = str(number)
                solveRek(board, empty_squares, index + 1)
                if solved:
                    return

            board[row][coll] = "."

        #############
        #   core    #
        #############

        solved = False
        empty_squares = emptySquares(board)
        solveRek(board, empty_squares)

def printBoard(board):
    for l in range(3):
        for k in range(3):
            row = board[3*l + k]
            for i in range(3):
                for j in range(3):
                    print(row[3*i+j], end=" ")
                print(end="\t")
            print()
        print()



if __name__ == "__main__":
    test = Solution()
    board = [["5","3",".",  ".","7",".",    ".",".","."]
            ,["6",".",".",  "1","9","5",    ".",".","."]
            ,[".","9","8",  ".",".",".",    ".","6","."]

            ,["8",".",".",  ".","6",".",    ".",".","3"]
            ,["4",".",".",  "8",".","3",    ".",".","1"]
            ,["7",".",".",  ".","2",".",    ".",".","6"]

            ,[".","6",".",  ".",".",".",    "2","8","."]
            ,[".",".",".",  "4","1","9",    ".",".","5"]
            ,[".",".",".",  ".","8",".",    ".","7","9"]]
    
    print("sudoku:\n")
    printBoard(board)
    test.solveSudoku(board)
    print("solved:\n")
    printBoard(board)
