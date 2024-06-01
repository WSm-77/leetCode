class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        def canBeCompleted(course) -> bool:
            nonlocal order, finished, prerequisitesGraph, orderIdx

            finished[course] = 1

            for nextCourse in prerequisitesGraph[course]:

                # we found cycle in current DFS instance
                if finished[nextCourse] == 1:
                    return False
                
                # se complete next course, if we haven't completed it yet
                elif finished[nextCourse] == 0:
                    if not canBeCompleted(nextCourse):
                        return False
            
            finished[course] = 2
            order[orderIdx] = course
            orderIdx -= 1

            return True
        # end def

        prerequisitesGraph = Solution.makeGraph(prerequisites, numCourses)

        # 0 - not finished, 1 - precessed in current DFS instance, 2 - processed (finished)
        finished = [0 for _ in range(numCourses)]
        order = [None for _ in range(numCourses)]
        orderIdx = numCourses - 1

        for course in range(numCourses):
            if finished[course] == 0:
                if not canBeCompleted(course):
                    return []
        
        return order

    
    @staticmethod
    def makeGraph(edges, V):
        graph = [[] for _ in range(V)]

        for neighbour, vertex in edges:
            graph[vertex].append(neighbour)

        return graph
    
if __name__ == "__main__":
    test = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    print(test.findOrder(numCourses, prerequisites))

    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(test.findOrder(numCourses, prerequisites))