from queue import PriorityQueue

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = Solution.makeGraph(times, n)

        INF = float("inf")
        minTime = 0
        visitedCnt = 0
        reciveTimes = [INF for _ in range(n)]
        toCheck = PriorityQueue()
        toCheck.put((0, k - 1))

        while not toCheck.empty():
            reciveTime, vertex = toCheck.get()

            if reciveTime < reciveTimes[vertex]:
                reciveTimes[vertex] = reciveTime
                minTime = max(minTime, reciveTime)
                visitedCnt += 1

                for neighbour, cost in graph[vertex]:
                    newTime = reciveTime + cost
                    if newTime < reciveTimes[neighbour]:
                        toCheck.put((newTime, neighbour))

        return minTime if visitedCnt == n else -1
    
    @staticmethod
    def makeGraph(edges, V):
        graph = [[] for _ in range(V)]

        for vertex, neighbour, cost in edges:
            graph[vertex - 1].append((neighbour - 1, cost))
        
        return graph
    
if __name__ == "__main__":
    test = Solution()
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    print(test.networkDelayTime(times, n, k))

    times = [[1,2,1]]
    n = 2
    k = 2
    print(test.networkDelayTime(times, n, k))