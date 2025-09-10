from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        k = self.get_k(nums)

        return nums[k]

    def get_k(self, nums):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1

        return left  % len(nums)

if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,5,1,2]
    res = sol.findMin(nums)
    print(res)
    assert res == min(nums)

    nums = [4,5,6,7,0,1,2]
    res = sol.findMin(nums)
    print(res)
    assert res == min(nums)

    nums = [11,13,15,17]
    res = sol.findMin(nums)
    print(res)
    assert res == min(nums)
