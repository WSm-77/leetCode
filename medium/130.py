class Solution:
    def solve(self, board: list[list[str]]) -> None:
        def dfs_visit(row, coll):
            nonlocal rows, colls, board, visited, directions

            visited[row][coll] = True

            for x, y in directions:
                newRow = row + x
                newColl = coll + y
                if not (0 <= newRow < rows and 0 <= newColl < colls):
                    continue

                if not visited[newRow][newColl] and board[newRow][newColl] == "O":
                    dfs_visit(newRow, newColl)

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        rows = len(board)
        colls = len(board[0])

        visited = [[False for _ in range(colls)] for _ in range(rows)]

        # visit all "O" connected to the board border and their neighbours
        for row in range(rows):
            if not visited[row][0] and board[row][0] == "O":
                dfs_visit(row, 0)
            
            if not visited[row][colls - 1] and board[row][colls - 1] == "O":
                dfs_visit(row, colls - 1)
        
        for coll in range(1, colls - 1):
            if not visited[0][coll] and board[0][coll] == "O":
                dfs_visit(0, coll)

            if not visited[rows - 1][coll] and board[rows - 1][coll] == "O":
                dfs_visit(rows - 1, coll)

        # not visited cells are captured
        for R in range(rows):
            for C in range(colls):
                if not visited[R][C]:
                    board[R][C] = "X"

if __name__ == "__main__":
    test = Solution()
    board = [["X","X","X","X"],
             ["X","O","O","X"],
             ["X","X","O","X"],
             ["X","O","X","X"]]
    print(*board, sep="\n")
    test.solve(board)
    print()
    print(*board, sep="\n")