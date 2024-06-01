from random import randint

##################
# first solution #
##################

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        windoWStart = 0
        currentSum = numbers[0] + numbers[1]
        while currentSum < target:
            windoWStart += 1
            currentSum = numbers[windoWStart] + numbers[windoWStart + 1]

        windowEnd = 1
        while target != currentSum:
            if currentSum < target:
                windowEnd += 1
            else:
                windoWStart -= 1
        currentSum = numbers[windoWStart] + numbers[windowEnd]


        return [windoWStart + 1, windowEnd + 1]

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
    test = Solution()
    numArray = [randint(0, 15) for _ in range(10)]
    numArray = sorted(numArray)
    print(numArray)
    targetSum = int(input("enter target sum: "))
    print(test.twoSum(numArray, targetSum))