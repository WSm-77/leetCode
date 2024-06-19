class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1 for _ in range(n)]

        product = 1
        for i in range(n):
            result[i] = product
            product *= nums[i]

        product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result
    
if __name__ == "__main__":
    nums = [1,2,3,4]
    test = Solution()
    print(test.productExceptSelf(nums))
    
    nums = [-1,1,0,-3,3]
    print(test.productExceptSelf(nums))