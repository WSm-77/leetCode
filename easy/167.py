from random import randint

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

if __name__ == "__main__":
    numArray = [randint(0, 15) for _ in range(10)]
    numArray = sorted(numArray)
    print(numArray)
    targetSum = int(input("enter target sum: "))
    print(sum2(numArray, targetSum))