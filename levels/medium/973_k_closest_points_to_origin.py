class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pointsLen = len(points)
        indicies = [i for i in range(pointsLen)]
        distances = [x*x + y*y for x, y in points]      # no taking sqrt of these valuse doesn't matter

        # performing quickselect for k-th element closest to origin positions k-1 points with
        # smaller distance to origin at lower indiecies than k
        self.quickSelect(indicies, distances, k - 1)

        return [points[indicies[x]] for x in range(k)]

    def quickSelect(self, indicies, distances, k):
        def calcDist(idx):
            return distances[indicies[idx]]

        def partition(beg, end):
            pivot = end
            i = beg
            for j in range(beg, end):
                if calcDist(j) <= calcDist(pivot):
                    indicies[i], indicies[j] = indicies[j], indicies[i]
                    i += 1
            indicies[pivot], indicies[i] = indicies[i], indicies[pivot]
            return i

        beg, end = 0, len(indicies) - 1
        while beg <= end:
            pivot = partition(beg, end)
            if pivot == k:
                break
            elif pivot < k:
                beg = pivot + 1
            else:
                end = pivot - 1

if __name__ == "__main__":
    test = Solution()
    # points = [[1,3],[-2,2]]
    # k = 1
    # print(test.kClosest(points, k))
    # points = [[3,3],[5,-1],[-2,4]]
    # k = 2
    # print(test.kClosest(points, k))
    points = [[6,10],[-3,3],[-2,5],[0,2]]
    k = 3
    print(test.kClosest(points, k))
