###############
# brute force #
###############

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        listLen = len(nums)
        secondIndex = firstIndex = 0
        for fIndex in range(listLen - 1):
            for sIndex in range(fIndex + 1, listLen):
                if nums[fIndex] + nums[sIndex] == target:
                    firstIndex = fIndex
                    secondIndex = sIndex
                    break

        return [firstIndex, secondIndex]

############
# one pass #
############

class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        listLen = len(nums)
        missingSum = [target - nums[0]]
        firstEleIndex = secondEleIndex = 0
        ele = 1
        found = False
        while not found and ele < listLen:
            for index in range(len(missingSum)):
                if missingSum[index] == nums[ele]:
                    firstEleIndex = index
                    secondEleIndex = ele
                    found = True
                    break
                #end if
            #end for
            missingSum.append(target - nums[ele])
            ele += 1
        #end while
        return [firstEleIndex, secondEleIndex]


if __name__ == "__main__":
    myObject = Solution
    myNums = [2,7,11,15]
    print(myObject.twoSum(myObject,myNums, 22))
    myObject2 = Solution2
    print(myObject2.twoSum(myObject2,myNums, 22))