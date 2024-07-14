class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1Len = len(s1)
        s2Len = len(s2)
        s3Len = len(s3)

        if s1Len + s2Len != s3Len:
            return False
        elif s1 == "":
            return s2 == s3
        elif s2 == "":
            return s1 == s3

        f = [[None for _ in range(s1Len)] for _ in range(s3Len)]
        g = [[None for _ in range(s2Len)] for _ in range(s3Len)]

        def backtrack(i, j, tab1, tab2, str1, str2):
            if tab1[i][j] == None:
                if j < 0:
                    return False
                if i == 0:
                    tab1[0][0] = str1[0] == s3[0]
                else:
                    tab1[i][j] = str1[j] == s3[i] and (backtrack(i - 1, j - 1, tab1, tab2, str1, str2)  or \
                                 backtrack(i - 1, i - j - 1, tab2, tab1, str2, str1))
            return tab1[i][j]

        return backtrack(s3Len - 1, s1Len - 1, f, g, s1, s2) or backtrack(s3Len - 1, s2Len - 1, g, f, s2, s1)

if __name__ == "__main__":
    test = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(test.isInterleave(s1, s2, s3))
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(test.isInterleave(s1, s2, s3))
    s1 = ""
    s2 = ""
    s3 = ""
    print(test.isInterleave(s1, s2, s3))