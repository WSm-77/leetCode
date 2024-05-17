class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        INF = float("inf")
        minCosts = [INF for _ in range(n+1)]
        minCosts[0] = minCosts[1] = 0

        for i in range(n-1):
            minCosts[i+1] = min(minCosts[i+1], minCosts[i] + cost[i])
            minCosts[i+2] = min(minCosts[i+2], minCosts[i] + cost[i])
        
        minCosts[n] = min(minCosts[n], minCosts[n - 1] + cost[n - 1])
        return minCosts[n]
    
if __name__ == "__main__":
    test = Solution()
    cost = [10,15,20]
    print(test.minCostClimbingStairs(cost))
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(test.minCostClimbingStairs(cost))