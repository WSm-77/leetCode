from queue import PriorityQueue

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        graph = [[] for _ in range(n)]

        for city, neighbour, cost in flights:
            graph[city].append((neighbour, cost))

        
        # prices[i][j] - cheapes travel cost from src to i-th city with j-stops
        prices = [[INF for _ in range(k + 1)] for _ in range(n)]
        for i in range(1, k+1):
            prices[src][i] = 0
        
        # 0 - price, 1 - city, 2 - stops
        toCheck = PriorityQueue()

        for neighbour, cost in graph[src]:
            toCheck.put((cost, neighbour, 0))

        while not toCheck.empty():
            price, city, stops = toCheck.get()
            if price >= prices[city][stops]:
                continue

            prices[city][stops] = price

            if stops == k:
                continue

            for neighbour, cost in graph[city]:
                newPrice = price + cost
                if newPrice < prices[neighbour][stops + 1]:
                    toCheck.put((newPrice, neighbour, stops + 1))
        
        minPrice = min(prices[dst])

        return minPrice if minPrice != INF else -1

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