class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        stringLen = len(s)
        patternLen = len(p)

        dp = {}

        def backtrack(patternIdx, strIdx):
            key = (patternIdx, strIdx)

            if key not in dp:
                if strIdx == -1:
                    if patternIdx == -1:
                        return True
                    elif p[patternIdx] == '*':
                        dp[key] = backtrack(patternIdx - 2, strIdx)
                        return dp[key]
                    else:
                        return False
                if patternIdx == -1:
                    return False

                if p[patternIdx] == '*':
                    if p[patternIdx - 1] == '.' or p[patternIdx - 1] == s[strIdx]:
                        dp[key] = backtrack(patternIdx, strIdx - 1) or backtrack(patternIdx - 2, strIdx)
                    else:
                        dp[key] = backtrack(patternIdx - 2, strIdx)
                elif p[patternIdx] == '.' or p[patternIdx] == s[strIdx]:
                    dp[key] = backtrack(patternIdx - 1, strIdx - 1)
                else:
                    dp[key] = False
            return dp[key]

        return backtrack(patternLen - 1, stringLen - 1)

if __name__ == "__main__":
    test = Solution()
    s = "aa"
    p = "aa"
    print(test.isMatch(s, p))   # True
    s = "aa"
    p = "a"
    print(test.isMatch(s, p))   # False
    s = "aa"
    p = "a*"
    print(test.isMatch(s, p))   # True
    s = "ab"
    p = ".*"
    print(test.isMatch(s, p))   # True
    s = "abakldsjfla"
    p = ".*"
    print(test.isMatch(s, p))   # True
    s = "aaab"
    p = "a.b"
    print(test.isMatch(s, p))   # False
    s = "aab"
    p = "c*a*b"
    print(test.isMatch(s, p))   # True
