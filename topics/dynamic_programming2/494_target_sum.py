class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        newTarget = sum(nums) + abs(target)
        if newTarget % 2 != 0:
            return 0
        newTarget //= 2
        dp = [[0 for _ in range(newTarget+1)] for _ in range(n)]

        dp[0][0] = 1
        if nums[0] > newTarget:
            return 0

        dp[0][nums[0]] += 1

        for numIdx in range(1, n):
            num = nums[numIdx]
            if num > newTarget:
                return 0
            for val in range(num):
                dp[numIdx][val] = dp[numIdx - 1][val]
            for val in range(num, newTarget+1):
                dp[numIdx][val] = dp[numIdx - 1][val] + dp[numIdx - 1][val - num]
        return dp[n - 1][newTarget]

if __name__ == "__main__":
    test = Solution()
    nums = [1,1,1,1,1]
    target = 3
    print(test.findTargetSumWays(nums, target))
    nums = [1]
    target = 1
    print(test.findTargetSumWays(nums, target))
    nums = [1, 7, 1]
    target = 1
    print(test.findTargetSumWays(nums, target))
    nums = [1000]
    target = -1000
    print(test.findTargetSumWays(nums, target))
