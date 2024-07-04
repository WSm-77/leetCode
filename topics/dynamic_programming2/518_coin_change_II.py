class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)

        # dp[val][c] - number of ways it is possible to achieve "val" amount of money only by using
        # coins[0], ..., coins[c]
        # dp = [[0 for _ in range(n)] for _ in range(amount+1)]
        # dp[val][c] = dp[val][c - 1] + dp[val - coins[c]][c]
        # to save some memory we use only two "rows"
        dp = [0 for _ in range(amount+1)]
        nextDp = [0 for _ in range(amount+1)]

        for val in range(amount+1):
            if val % coins[0] == 0:
                dp[val] = nextDp[val] = 1

        for coinIdx in range(1, n):
            coin = coins[coinIdx]
            for val in range(amount+1):
                nextDp[val] = dp[val]
                prevVal = val - coin
                if 0 <= prevVal:
                    nextDp[val] += nextDp[prevVal]
            dp, nextDp = nextDp, dp

        return dp[amount]

if __name__ == "__main__":
    test = Solution()
    amount = 5
    coins = [1,2,5]
    print(test.change(amount, coins))
    amount = 3
    coins = [2]
    print(test.change(amount, coins))
