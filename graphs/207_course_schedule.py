class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        finished = [False for _ in range(numCourses)]

        prerequisitesGraph = Solution.createGraph(prerequisites, numCourses)

        order = Solution.topoSort(prerequisitesGraph)

        for course in order:
            finished[course] = True
            for prerequisite in prerequisitesGraph[course]:
                if finished[prerequisite]:
                    return False

        return True

    @staticmethod
    def topoSort(graph):
        def dfs_visit(vertex):
            nonlocal visited, graph, order, orderIdx

            visited[vertex] = True

            for neighbour in graph[vertex]:
                if not visited[neighbour]:
                    dfs_visit(neighbour)

            order[orderIdx] = vertex
            orderIdx -= 1

        V = len(graph)
        visited = [False for _ in range(V)]

        order = [None for _ in range(V)]
        orderIdx = V - 1

        for vertex in range(V):
            if not visited[vertex]:
                dfs_visit(vertex)

        return order

    @staticmethod
    def createGraph(edges, V):
        graph = [[] for _ in range(V)]

        for vertex, neighbour in edges:
            graph[vertex].append(neighbour)

        return graph

if __name__ == "__main__":
    test = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    print(test.canFinish(numCourses, prerequisites))

    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(test.canFinish(numCourses, prerequisites))

    numCourses = 5
    prerequisites = [[1,4],[2,4],[3,1],[3,2]]
    print(test.canFinish(numCourses, prerequisites))
    