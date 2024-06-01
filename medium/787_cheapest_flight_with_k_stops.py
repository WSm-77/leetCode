from queue import PriorityQueue

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        prices = [INF for _ in range(n)]
        prices[src] = 0
        tmpPrices = [INF for _ in range(n)]

        for _ in range(k+1):
            for i in range(n):
                tmpPrices[i] = prices[i]

            for city, neighbour, cost in flights:
                newPrice = prices[city] + cost
                if newPrice < tmpPrices[neighbour]:
                    tmpPrices[neighbour] = newPrice
            
            for i in range(n):
                prices[i] = tmpPrices[i]
        
        return prices[dst] if prices[dst] != INF else -1


if __name__ == "__main__":
    test = Solution()
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    print(test.findCheapestPrice(n, flights, src, dst, k))

    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    print(test.findCheapestPrice(n, flights, src, dst, k))

    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    print(test.findCheapestPrice(n, flights, src, dst, k))