def windowMax(numArray):
    arrayLen = len(numArray)
    maxSum = numArray[0] 
    currentSum = 0
    for i in range(arrayLen):
        if currentSum < 0:
            currentSum = 0
        currentSum += numArray[i]
        maxSum = max(maxSum, currentSum)
    return maxSum    

def quadraticMax(numArray):
    arrayLen = len(numArray)
    maxSum = numArray[0]
    for i in range(arrayLen):
        currentSum = 0
        for j in range(i, arrayLen):
            currentSum += numArray[j]
            maxSum = max(maxSum, currentSum)
        #end for
    #end for
    return maxSum

if __name__ == "__main__":
    numArray = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # print(quadraticMax(numArray))
    print(windowMax(numArray))