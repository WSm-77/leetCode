# substring created by letters from j-th index to i-th index is palindrom if substring created by letters from
# (j+1)-th index to (i-1)-th index is palindrom and letters at i-th and j-th indexes are the same.
#
# Example string: "cabbad"
# to check if s[1:4+1] ("abba") is palindrom we check if "bb" is palindrom and if "a" == "a"

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        isPalindrom = [[True for _ in range(n)] for _ in range(n)]

        palindromCnt = n

        for i in range(1, n):
            for j in range(i):
                isPalindrom[i][j] = isPalindrom[i - 1][j + 1] and s[i] == s[j]
                palindromCnt += int(isPalindrom[i][j])

        return palindromCnt

if __name__ == "__main__":
    test = Solution()
    s = "abc"
    print(test.countSubstrings(s))
    s = "aaa"
    print(test.countSubstrings(s))
