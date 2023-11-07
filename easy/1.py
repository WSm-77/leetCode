def twoSum(nums: list[int], target: int) -> list[int]:
    listLen = len(nums)
    secondIndex = firstIndex = 0
    for fIndex in range(listLen - 1):
        for sIndex in range(fIndex + 1, listLen):
            if nums[fIndex] + nums[sIndex] == target:
                firstIndex = fIndex
                secondIndex = sIndex
                break

    return [firstIndex, secondIndex]

myNums = [2,7,11,15]
print(twoSum(myNums, 22))