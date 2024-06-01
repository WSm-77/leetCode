from math import ceil

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        piles.sort()
        
        minK = 1
        maxK = piles[n - 1]

        while abs(minK - maxK) >= 1:
            mid = (minK + maxK) // 2
            if Solution.get_sum(piles, mid) > h:
                minK = mid + 1
            else:
                maxK = mid

        return minK

    def get_sum(piles, k):
        mySum = 0
        for pile in piles:
            mySum += ceil(pile/k)

        return mySum

if __name__ == "__main__":
    testTab = [30,11,23,4,20]
    h = 5
    test = Solution()
    print(test.minEatingSpeed(testTab, h))
    
    testTab = [30,11,23,4,20]
    h = 6
    print(test.minEatingSpeed(testTab, h))