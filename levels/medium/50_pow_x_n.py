class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        negaitve = n < 0
        n = abs(n)

        mul = x

        while n > 0:
            if n % 2 == 1:
                res *= mul

            n //= 2
            mul *= mul

        if negaitve:
            res = 1 / res

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2, 5))
    print(sol.myPow(2, -5))
