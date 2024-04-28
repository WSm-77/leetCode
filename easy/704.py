class Solution:
    def search(self, nums: list[int], target: int) -> int:
        beg = 0
        end = len(nums) - 1
        while beg <= end:
            mid = (beg + end) // 2
            if nums[mid] < target:
                beg = mid + 1
            else:
                end = mid - 1
        
        return beg