class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        # max profit after "i" days
        profit = [0 for _ in range(n)]

        # max profit after "i" days, if we buy at i-th day
        buy = [0 for _ in range(n)]

        # max profit after "i" days, if we sell at i-th day
        sell = [0 for _ in range(n)]
        
        # max profit after "i" days, if we don't do any action at i-th day and we don't possess any stock
        cooldown = [0 for _ in range(n)]

        buy[0] = -prices[0]

        for i in range(1, n):
            buy[i] = max(buy[i-1], max(cooldown[i-1], 0) - prices[i])
            sell[i] = buy[i-1] + prices[i]
            cooldown[i] = max(cooldown[i-1], sell[i-1])
            profit[i] = max(profit[i-1], sell[i])
        
        return profit[n - 1]
    
if __name__ == "__main__":
    test = Solution()
    prices = [1,2,3,0,2]
    print(test.maxProfit(prices))   # answer: 3
    prices = [1]
    print(test.maxProfit(prices))   # answer: 0
    prices = [4,2,7,1,11]
    print(test.maxProfit(prices))   # answer: 10
    prices = [6,1,6,4,3,0,2]
    print(test.maxProfit(prices))   # answer: 7
        