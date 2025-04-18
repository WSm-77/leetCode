from typing import List

##################
# first solution #
##################

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        nums_set = set(nums)

        for val in range(n + 1):
            if val not in nums_set:
                return val

###################
# second solution #
###################

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num

        return res
