import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)

            if stone1 != stone2:
                heapq.heappush(stones, -(stone1 - stone2))

        return -heapq.heappop(stones) if len(stones) == 1 else 0

if __name__ == "__main__":
    test = Solution()
    stones = [2,7,4,1,8,1]
    print(test.lastStoneWeight(stones))
    stones = [1]
    print(test.lastStoneWeight(stones))
