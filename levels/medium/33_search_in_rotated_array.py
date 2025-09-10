from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = self.get_k(nums)

        left = k
        right = (k - 1) % len(nums)

        or_left = self.idx_to_original(nums, left, k)
        or_right = self.idx_to_original(nums, right, k)

        while or_left <= or_right:

            or_mid = (or_left + or_right) // 2

            mid = self.original_to_idx(nums, or_mid, k)

            if nums[mid] < target:
                or_left = or_mid + 1
            else:
                or_right = or_mid - 1

        left = self.original_to_idx(nums, or_left, k)

        return left if nums[left] == target else -1

    def idx_to_original(self, nums, idx, k):
        return idx - k if idx >= k else idx - k + len(nums)

    def original_to_idx(self, nums, idx, k):
        return (idx + k) % len(nums)

    def get_k(self, nums):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1

        return left % len(nums)

if __name__ == "__main__":
    sol = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(sol.search(nums, target))
    nums = [4,5,6,7,0,1,2]
    target = 3
    print(sol.search(nums, target))
    nums = [1]
    target = 0
    print(sol.search(nums, target))
    nums = [3,1]
    target = 3
    print(sol.search(nums, target))
