class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)

        # f[i] - max product of any subarray that ends at i-th index
        f = [num for num in nums]
        # g[i] - min product of any subarray that ends at i-th index
        g = [num for num in nums]

        for i in range(1, n):
            num = nums[i]
            f[i] = max(f[i-1]*num, g[i-1]*num, f[i])
            g[i] = min(f[i-1]*num, g[i-1]*num, g[i])

        return max(f)

if __name__ == "__main__":
    test = Solution()
    nums = [2,3,-2,4]
    print(test.maxProduct(nums))
    nums = [-2,0,-1]
    print(test.maxProduct(nums))
