class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minStrLen = len(strs[0])
        for string in strs:
            currentLen = len(string)
            minStrLen = min(minStrLen, currentLen)
        #end for
        i = 0
        while i < minStrLen:
            currentLetter = strs[0][i]
            validLetter = True
            for string in strs:
                if string[i] != currentLetter:
                    validLetter = False
                    break
                #end if
            #end for
            if not validLetter:
                break
            else:
                i += 1
            #end if
        #end while
        return strs[0][:i]
    
if __name__ == "__main__":
    myObject = Solution
    strs = ["flower","flow","flight"]
    print(myObject.longestCommonPrefix(myObject, strs))