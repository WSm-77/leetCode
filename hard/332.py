class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        def dfs_visit(vertex: str):
            nonlocal graph, itinerary, itineraryIdx

            if vertex in graph:
                for neighbour in graph[vertex]:
                    if not neighbour[1]:
                        neighbour[1] = True
                        dfs_visit(neighbour[0])

            itinerary[itineraryIdx] = vertex
            itineraryIdx -= 1
        #end def
        
        E = len(tickets)
        graph: dict[str, list[list[int | bool]]] = {vertex : [] for vertex, neighbour in tickets}

        for vertex, neighbour in tickets:
            graph[vertex].append([neighbour, False])

        for vertex in graph:
            graph[vertex].sort(key=lambda x: x[0])

        itinerary = [None for _ in range(E + 1)]
        itineraryIdx = E

        dfs_visit("JFK")

        return itinerary
        

if __name__ == "__main__":
    test = Solution()
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(test.findItinerary(tickets))
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print(test.findItinerary(tickets))

