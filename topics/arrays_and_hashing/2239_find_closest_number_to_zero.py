from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]

        for num in nums:
          if abs(num) < abs(res):
            res = num
          elif abs(num) == abs(res) and res < num:
            res = num

        return res

if __name__ == "__main__":
  sol = Solution()
  nums = [-4,-2,1,4,8]
  print(sol.findClosestNumber(nums))
