class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b
        
        return b
    
if __name__ == "__main__":
    test = Solution()
    n = 2
    print(test.climbStairs(n))
    n = 3
    print(test.climbStairs(n))