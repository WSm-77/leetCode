class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)

        nums.sort()

        firstElem = 0
        result = []

        while firstElem + 2 < n and nums[firstElem] <= 0:
            beg = firstElem + 1
            end = n - 1

            targetSum = -nums[firstElem]

            # now we look for every unique set of two numbers that sum to targetSum 
            while beg < end:
                currentSum = nums[beg] + nums[end]
                if currentSum == targetSum:
                    result.append([nums[firstElem], nums[beg], nums[end]])
                    beg = Solution.update_indicie(nums, beg, 1, end)
                    end = Solution.update_indicie(nums, end, -1, beg)
                elif currentSum < targetSum:
                    beg += 1
                else:
                    end -= 1
            
            firstElem = Solution.update_indicie(nums, firstElem, 1, n - 2)

        return result
    
    @staticmethod
    def update_indicie(nums, idx, step, boundary):
        prevIdxVal = nums[idx]
        while idx != boundary and prevIdxVal == nums[idx]:
            idx += step
        
        return idx

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    test = Solution()
    print(test.threeSum(nums))
    nums = [0,0,0]
    print(test.threeSum(nums))
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    print(test.threeSum(nums))