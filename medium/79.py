class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(x, y, idx):
            nonlocal visited, n, m
            if board[x][y] != word[idx]:
                return False
            elif idx == len(word) - 1:
                return True
            
            visited[x][y] = True
            currentWord.append(board[x][y])

            if 0 <= x - 1 and not visited[x - 1][y]:
                if dfs(x - 1, y, idx + 1):
                    return True
            if x + 1 < n and not visited[x + 1][y]:
                if dfs(x + 1, y, idx + 1):
                    return True
            if 0 <= y - 1 and not visited[x][y - 1]:
                if dfs(x, y - 1, idx + 1):
                    return True
            if y + 1 < m and not visited[x][y + 1]:
                if dfs(x, y + 1, idx + 1):
                    return True

            visited[x][y] = False
            currentWord.pop()

            return False
        #end def
        
        n = len(board)
        m = len(board[0])

        visited = [[False for _ in range(m)] for _ in range(n)]
        currentWord: list[str] = []

        for R in range(n):
            for C in range(m):
                if dfs(R, C, 0):
                    return True
        
        return False
    
if __name__ == "__main__":
    test = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(test.exist(board, word))
    word = "SEE"
    print(test.exist(board, word))
    word = "ABCB"
    print(test.exist(board, word))