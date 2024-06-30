class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        subsetSum = sum(nums)
        if subsetSum % 2 != 0:
            return False
        subsetSum //= 2

        # dp[currSum] - is it possible to achieve currSum if we consider only nums in range 0 ~ i
        dp = [False for _ in range(subsetSum+1)]
        dp2 = [False for _ in range(subsetSum+1)]

        dp[0] = True
        if nums[0] <= subsetSum:
            dp[nums[0]] = True

        for i in range(1, n):
            num = nums[i]
            for currSum in range(min(num, subsetSum+1)):
                dp2[currSum] = dp[currSum]
            for currSum in range(num, subsetSum+1):
                dp2[currSum] = dp[currSum - num] or dp[currSum]
            dp, dp2 = dp2, dp

        return dp[subsetSum]
    
if __name__ == "__main__":
    test = Solution()
    nums = [1,5,11,5]
    print(test.canPartition(nums))
    nums = [1,2,3,5]
    print(test.canPartition(nums))
    nums = [3,3,3,4,5]
    print(test.canPartition(nums))
    nums = [1,5,10,6]
    print(test.canPartition(nums))
