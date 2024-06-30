class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m ~ rows
        # n ~ colls

        # dp[R][C] how many paths exist to reach (R, C) cell in grid
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            # we can come only from "up"
            dp[i][0] = 1

        for i in range(n):
            # we can come only from "left"
            dp[0][i] = 1
        
        for row in range(1, m):
            for coll in range(1, n):
                # we can come from "up" either from "left"
                dp[row][coll] = dp[row - 1][coll] + dp[row][coll - 1]
        
        return dp[m - 1][n - 1]
    
if __name__ == "__main__":
    test = Solution()
    m = 3
    n = 7
    print(test.uniquePaths(m, n))
    m = 3
    n = 2
    print(test.uniquePaths(m, n))
        