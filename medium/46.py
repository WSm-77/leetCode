class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def rek(toUse: list[int]):
            nonlocal result, used
            if len(toUse) == 0:
                result.append(used.copy())
                return

            for i in range(len(toUse)):
                left = toUse[:i]
                right = toUse[i+1:]
                used.append(toUse[i])
                rek(left + right)
                used.pop()
        #end def

        used = []
        result = []
        rek(nums)
        return result

if __name__ == "__main__":
    test = Solution()
    nums = [1,2,3]
    print(test.permute(nums))
    nums = [0,1]
    print(test.permute(nums))
    nums = [0]
    print(test.permute(nums))