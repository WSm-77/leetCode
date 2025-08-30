from typing import List

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    res = nums[0]
    curr_sum = 0

    for num in nums:
      curr_sum += num
      res = max(res, curr_sum)

      if curr_sum < 0:
        curr_sum = 0
    return res

if __name__ == "__main__":
  sol = Solution()
  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  print(sol.maxSubArray(nums))
  nums = [1]
  print(sol.maxSubArray(nums))
  nums = [5, 4, -1, 7, 8]
  print(sol.maxSubArray(nums))
