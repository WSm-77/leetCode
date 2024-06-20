class Solution:
    def canJump(self, nums: list[int]) -> bool:
        lastIdx = len(nums) - 1
        maxRange = nums[0]

        idx = 0
        while idx <= maxRange:
            if idx == lastIdx:
                return True
            maxRange = max(maxRange, nums[idx] + idx)
            idx += 1
            
        return False
    
if __name__ == "__main__":
    test = Solution()
    nums = [2,3,1,1,4]
    print(test.canJump(nums))
    nums = [3,2,1,0,4]
    print(test.canJump(nums))

