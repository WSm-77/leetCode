##################
# first solution #
##################

class Solution:
    def isPalindrome(self, x: int) -> bool:
        revers = str(x)
        return revers == revers[::-1]
    
###################    
# second solution #
###################
class Solution2:
    def isPalindrome(x: int) -> bool:
        xCp = abs(x)
        palindrom = 0
        while 0 != xCp:
            palindrom = palindrom * 10 + xCp % 10
            xCp //= 10
        #end while
        return x == palindrom

print(Solution2.isPalindrome(x=-121))