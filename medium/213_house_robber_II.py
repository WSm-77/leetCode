###################
# O(n^2) solution #
###################

class Solution1:
    def rob(self, nums: list[int]) -> int:
        def rob_from_to(beg, end):
            nonlocal nums
            profit = [nums[i] for i in range(beg, end)]
            maxProfit = profit[0]

            for idx in range(beg, end):
                for prevIdx in range(beg, idx - 1):
                    newProfit = profit[prevIdx - beg] + nums[idx]
                    if profit[idx - beg] < newProfit:
                        profit[idx - beg] = newProfit
                maxProfit = max(maxProfit, profit[idx - beg])
            
            return maxProfit

        n = len(nums)

        return nums[0] if n == 1 else max(rob_from_to(0, n - 1), rob_from_to(1, n))
    
#################
# O(n) solution #
#################

class Solution2:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        # f - max profit for robing houses in range: 0 ~ i
        f = [nums[i] for i in range(n)]
        
        # g - max profit for robing houses in range: 0 ~ i, without robbing i-th house
        g = [0 for _ in range(n)]

        maxProfit = 0

        for i in range(1, n - 1):
            g[i] = f[i - 1]
            f[i] = max(g[i], nums[i] + g[i-1])
        
        maxProfit = f[n - 2]

        for i in range(n):
            f[i] = nums[i]
            g[i] = 0

        for i in range(2, n):
            g[i] = f[i - 1]
            f[i] = max(g[i], nums[i] + g[i-1])

        maxProfit = max(maxProfit, f[n - 1])

        return maxProfit
    
if __name__ == "__main__":
    test1 = Solution1()
    test2 = Solution2()
    nums = [2,3,2]
    print(test1.rob(nums), test2.rob(nums))
    nums = [1,2,3,1]
    print(test1.rob(nums), test2.rob(nums))
    nums = [1,2,3]
    print(test1.rob(nums), test2.rob(nums))
        



    
