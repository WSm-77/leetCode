class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        sums = [nums[0]]

        for i in range(1, n):
            sums.append(sums[i - 1] + nums[i])

        if sums[-1] - sums[0] == 0:
            return 0

        for pivot in range(1, n):
            sum_left = sums[pivot - 1]
            sum_right = sums[-1] - sums[pivot]

            if sum_left == sum_right:
                return pivot

        return -1
