class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)
        if slen != tlen:
            return False
        
        letters = {}

        for i in range(slen):
            SLetter = s[i]
            TLetter = t[i]
            if SLetter in letters:
                letters[SLetter] += 1
            else:
                letters[SLetter] = 1
            #end if
            if TLetter in letters:
                letters[TLetter] -= 1
            else:
                letters[TLetter] = -1
            #end if
        #end for
        if max(letters.values()) == 0:
            return True
        else:
            return False
        
if __name__ == "__main__":
    myObject = Solution
    s = "anagram"
    t = "nagaram"
    print(myObject.isAnagram(myObject,s,t))
    s = "rat"
    t = "car"
    print(myObject.isAnagram(myObject,s,t))