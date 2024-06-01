class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def rek(idx, currentSet):
            nonlocal result, n, nums
            if idx == n:
                result.append(currentSet)
                return

            rek(idx + 1, currentSet)
            rek(idx + 1, currentSet + [nums[idx]])

        n = len(nums)
        result = []
        rek(0, [])
        return result
    
if __name__ == "__main__":
    test = Solution()
    nums = [1,2,3]
    print(test.subsets(nums))
    nums = [0]
    print(test.subsets(nums))