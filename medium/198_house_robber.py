class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        maxProfit = nums[0]

        for house in range(1, n):
            cost = nums[house]
            for prevHouse in range(house - 1):
                if nums[prevHouse] + cost > nums[house]:
                    nums[house] = nums[prevHouse] + cost
            maxProfit = max(maxProfit, nums[house])
        
        return maxProfit
    
if __name__ == "__main__":
    test = Solution()
    nums = [1,2,3,1]
    print(test.rob(nums))
    nums = [2,7,9,3,1]
    print(test.rob(nums))