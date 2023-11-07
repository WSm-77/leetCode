from random import randint

##################
# first solution #
##################

def sum2(numArray, targetSum):
    arrayLen = len(numArray)
    windoWStart = 0
    currentSum = numArray[0] + numArray[1]
    while currentSum < targetSum:
        windoWStart += 1
        assert(windoWStart < arrayLen)
        currentSum = numArray[windoWStart] + numArray[windoWStart + 1]

    windowEnd = 1
    while targetSum != currentSum:
        if currentSum < targetSum:
            windowEnd += 1
        else:
            windoWStart -= 1
            assert(windoWStart < arrayLen)
            assert(windowEnd >= 0)
        currentSum = numArray[windoWStart] + numArray[windowEnd]


    return windoWStart + 1, windowEnd + 1

###################
# second solution #
###################

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        tabLen = len(numbers)
        firstIndex = 0
        secondIndex = tabLen - 1

        while secondIndex > firstIndex:
            currentSum = numbers[firstIndex] + numbers[secondIndex]
            if currentSum == target:
                return [firstIndex + 1, secondIndex + 1]
            elif currentSum > target:
                secondIndex -= 1
            else:
                firstIndex += 1

if __name__ == "__main__":
    numArray = [randint(0, 15) for _ in range(10)]
    numArray = sorted(numArray)
    print(numArray)
    targetSum = int(input("enter target sum: "))
    print(sum2(numArray, targetSum))