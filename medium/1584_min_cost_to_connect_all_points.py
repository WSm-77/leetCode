class FindUnion:
    def __init__(self, V) -> None:
        self.representants = [i for i in range(V)]
        self.ranks = [0 for _ in range(V)]

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
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        V = len(points)
        edges = self.createEdges(points)
        edges.sort(key=lambda x: x[2])
        sets = FindUnion(V)
        cost = 0
        connectedCnt = 1

        for vertex, neighbour, weight in edges:
            if sets.find(vertex) != sets.find(neighbour):
                sets.union(vertex, neighbour)
                cost += weight
                connectedCnt += 1
                if connectedCnt == V:
                    return cost

        return cost

    def createEdges(self, points):
        V = len(points)
        edges = []

        for vertex in range(V - 1):
            x1, y1 = points[vertex]
            for neighbour in range(vertex + 1, V):
                x2, y2 = points[neighbour]
                edges.append((vertex, neighbour, abs(x1 - x2) + abs(y1 - y2)))

        return edges

if __name__ == "__main__":
    test = Solution()
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(test.minCostConnectPoints(points))
    points = [[3,12],[-2,5],[-4,1]]
    print(test.minCostConnectPoints(points))