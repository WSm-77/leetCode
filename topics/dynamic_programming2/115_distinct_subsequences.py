class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sourceLen = len(s)
        targetLen = len(t)

        # dp[i][j] - number of possibilities of achieving substring t[:i+1] from first "j"
        # characters of string "s"
        # dp[i][j] = ...
        # 1) dp[i][j - 1]
        # 2) if i-th char is the same as j-ty char in target string: dp[i - 1][j - 1]
        dp = [[0 for _ in range(sourceLen)] for _ in range(targetLen)]

        if s[0] == t[0]:
            dp[0][0] = 1

        for i in range(1, sourceLen):
            dp[0][i] = dp[0][i-1]
            if s[i] == t[0]:
                dp[0][i] += 1

        for targetCharIdx in range(1, targetLen):
            for sourceCharIdx in range(targetCharIdx, sourceLen):
                dp[targetCharIdx][sourceCharIdx] = dp[targetCharIdx][sourceCharIdx - 1]
                if s[sourceCharIdx] == t[targetCharIdx]:
                    dp[targetCharIdx][sourceCharIdx] += dp[targetCharIdx - 1][sourceCharIdx - 1]

        return dp[targetLen - 1][sourceLen - 1]

if __name__ == "__main__":
    test = Solution()
    s = "rabbbit"
    t = "rabbit"
    print(test.numDistinct(s, t))
    s = "babgbag"
    t = "bag"
    print(test.numDistinct(s, t))
