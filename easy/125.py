class Solution:
    def isPalindrome(self, s: str) -> bool:
        beg = 0
        end = len(s) - 1

        while beg < end:
            if not s[end].isalnum():
                end -= 1
                continue
            elif not s[beg].isalnum():
                beg += 1
                continue

            if s[beg].lower() != s[end].lower():
                return False
            
            end -= 1
            beg += 1
        
        return True
    
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    test = Solution()
    print(test.isPalindrome(s))
    s = "race a car"
    print(test.isPalindrome(s))
    s = " "
    print(test.isPalindrome(s))
