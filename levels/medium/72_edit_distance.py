################################
# first solution (memoization) #
################################

class FirstSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        # source: word1
        # target: word2
        sourceLen = len(word1)
        targetLen = len(word2)

        # dp[i][j] - distance between strings word1[:i] and word2[:j]
        dp = [[None for _ in range(targetLen+1)] for _ in range(sourceLen+1)]

        def backtrack(i, j):
            if dp[i][j] != None:
                return dp[i][j]

            if i == 0 or j == 0:
                dp[i][j] = max(i, j)
                return dp[i][j]

            if word1[i-1] == word2[j-1]:
                # current character match each other
                dp[i][j] = backtrack(i - 1, j - 1)
            else:
                # replace
                dp[i][j] = backtrack(i - 1, j - 1) + 1
                # add
                dp[i][j] = min(dp[i][j], backtrack(i, j - 1) + 1)
                # remove
                dp[i][j] = min(dp[i][j], backtrack(i - 1, j) + 1)

            return dp[i][j]

        return backtrack(sourceLen, targetLen)

###############################
# second solution (bottom-up) #
###############################

class SecondSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        # source: word1
        # target: word2
        sourceLen = len(word1)
        targetLen = len(word2)

        # dp[i][j] - distance between strings word1[:i] and word2[:j]
        dp = [[None for _ in range(targetLen+1)] for _ in range(sourceLen+1)]

        for i in range(sourceLen + 1):
            dp[i][0] = i

        for j in range(1, targetLen + 1):
            dp[0][j] = j

        for i in range(1, sourceLen+1):
            for j in range(1, targetLen+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        # print(*dp, sep="\n")

        return dp[sourceLen][targetLen]

if __name__ == "__main__":
    firstSolutionTest = FirstSolution()
    secondSolutionTest = SecondSolution()
    word1 = "horse"
    word2 = "ros"
    print(firstSolutionTest.minDistance(word1, word2))
    print(secondSolutionTest.minDistance(word1, word2))

    word1 = "intention"
    word2 = "execution"
    print(firstSolutionTest.minDistance(word1, word2))
    print(secondSolutionTest.minDistance(word1, word2))

    word1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
    word2 = "ultramicroscopically"
    print(firstSolutionTest.minDistance(word1, word2))
    print(secondSolutionTest.minDistance(word1, word2))