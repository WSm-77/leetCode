class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        strLen = len(s)

        if strLen == 1:
            return symbols[s[0].upper()]
        #end if
        decimalNum = 0
        i = 1
        prevNum = 0
        currentNum = symbols[s[0].upper()]
        while i < strLen:
            prevNum, currentNum = currentNum, symbols[s[i].upper()]
            if prevNum < currentNum:
                prevNum = -prevNum
            #end if

            decimalNum += prevNum
            i += 1
        #end while
        decimalNum += currentNum

        return decimalNum
    
if __name__ == "__main__":
    myObj = Solution
    s = 'III'
    print(myObj.romanToInt(myObj, s))

    s = 'XIV'
    print(myObj.romanToInt(myObj, s))

    s = "LVIII"
    print(myObj.romanToInt(myObj, s))

    s = "MCMXCIV"
    print(myObj.romanToInt(myObj, s))