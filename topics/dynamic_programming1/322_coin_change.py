class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)

        INF = float("inf")
        fewestCoins = [INF for _ in range(amount+1)]
        fewestCoins[0] = 0

        for coin in coins:
            for value in range(coin, amount + 1): 
                fewestCoins[value] = min(fewestCoins[value], fewestCoins[value - coin] + 1)
        
        return fewestCoins[-1] if fewestCoins[-1] != INF else -1
    
if __name__ == "__main__":
    test = Solution()
    coins = [1,2,5]
    amount = 11
    print(test.coinChange(coins, amount))
    coins = [2]
    amount = 3
    print(test.coinChange(coins, amount))
    coins = [1]
    amount = 0
    print(test.coinChange(coins, amount))

