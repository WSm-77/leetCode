class FindUnion:
    def __init__(self, V):
        self.representants = [i for i in range(V+1)]
        self.ranks = [0 for _ in range(V+1)]

    def find(self, ele):
        if self.representants[ele] != ele:
            self.representants[ele] = self.find(self.representants[ele])
        return self.representants[ele]
    
    def union(self, ele1, ele2):
        repr1 = self.find(ele1)
        repr2 = self.find(ele2)

        if repr1 == repr2:
            return
        
        if self.ranks[repr1] < self.ranks[repr2]:
            self.representants[repr1] = repr2
        else:
            self.representants[repr2] = repr1
            if self.ranks[repr1] == self.ranks[repr2]:
                self.ranks[repr1] += 1

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        V = self.getNumberOfVerticies(edges)
        sets = FindUnion(V)
        for vertex, neighbour in edges:
            if sets.find(vertex) == sets.find(neighbour):
                return [vertex, neighbour]
            
            sets.union(vertex, neighbour)

    def getNumberOfVerticies(self, edges):
        V = 0
        for vertex, neighbour in edges:
            V = max(V, vertex, neighbour)
        return V

if __name__ == "__main__":
    test = Solution()
    edges = [[1,2],[1,3],[2,3]]
    print(test.findRedundantConnection(edges))
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    print(test.findRedundantConnection(edges))
