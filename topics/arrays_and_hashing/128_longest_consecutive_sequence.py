class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numsSet = set(nums)

        result = 0
        for num in nums:
            if num - 1 not in numsSet:
                sequenceLength = 1
                while (num + sequenceLength) in numsSet:
                    sequenceLength += 1
                if sequenceLength > result:
                    result = sequenceLength
        
        return result
    
if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    test = Solution()
    print(test.longestConsecutive(nums))
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(test.longestConsecutive(nums))