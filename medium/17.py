class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def backrack(digitIdx, currentWord):
            nonlocal digits, digitToLetters
            if digitIdx == len(digits):
                result.append(currentWord)
                return

            for letter in digitToLetters[digits[digitIdx]]:
                backrack(digitIdx + 1, currentWord + letter)
        #end def

        if len(digits) == 0:
            return []

        digitToLetters = {"2": "abc",
                          "3": "def",
                          "4": "ghi",
                          "5": "jkl",
                          "6": "mno",
                          "7": "pqrs",
                          "8": "tuv",
                          "9": "wxyz"}

        result = []
        backrack(0, "")

        return result

if __name__ == "__main__":
    test = Solution()
    digits = "23"
    print(test.letterCombinations(digits))
    digits = ""
    print(test.letterCombinations(digits))
    digits = "2"
    print(test.letterCombinations(digits))
