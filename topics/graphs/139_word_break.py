class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        strLen = len(s)
        dictLen = len(wordDict)

        canBeSplit = [False for _ in range(strLen+1)]
        canBeSplit[0] = True

        for strIdx in range(1, strLen+1):
            for i in range(1, dictLen+1):
                word = wordDict[i-1]
                wordLen = len(word)
                if strIdx < wordLen or not canBeSplit[strIdx-wordLen]:
                    continue
                if s[strIdx-wordLen:strIdx] == word:
                    canBeSplit[strIdx] = True
                    break

        return canBeSplit[strIdx]

if __name__ == "__main__":
    test = Solution()
    s = "leetcode"
    wordDict = ["leet","code"]
    print(test.wordBreak(s, wordDict))
    s = "applepenapple"
    wordDict = ["apple","pen"]
    print(test.wordBreak(s, wordDict))
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(test.wordBreak(s, wordDict))
