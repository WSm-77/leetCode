class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        def rek(idx):
            nonlocal result, currentSubSet
            # print()
            if idx == n:
                result.append(currentSubSet[:])
                return

            nextIdx = idx
            while nextIdx < n and nums[nextIdx] == nums[idx]:
                nextIdx += 1
                currentSubSet.append(nums[idx])
            #end while

            for _ in range(idx, nextIdx):
                rek(nextIdx)
                currentSubSet.pop()

            rek(nextIdx)
        #end def

        n = len(nums)
        nums.sort()
        result = []
        currentSubSet = []
        rek(0)

        return result

if __name__  == "__main__":
    test = Solution()
    nums = [1,2,2]
    print(sorted(test.subsetsWithDup(nums)))
    nums = [0]
    print(sorted(test.subsetsWithDup(nums)))
    nums = [4,4,4,1,4]
    print(sorted(test.subsetsWithDup(nums)))