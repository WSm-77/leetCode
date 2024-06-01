from queue import PriorityQueue

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        toCheck = PriorityQueue()
        toCheck.put((grid[0][0], 0, 0))

        while not toCheck.empty():
            cost, row, coll = toCheck.get()

            if grid[row][coll] < 0:
                continue

            if row == coll == n - 1:
                return cost

            # mark visited
            grid[row][coll] *= -1

            for neighbourRow, neighbourColl in self.neighbours(row, coll, n):
                if grid[neighbourRow][neighbourColl] < 0:
                    continue
                if grid[neighbourRow][neighbourColl] < cost:
                    toCheck.put((cost, neighbourRow, neighbourColl))
                else:
                    toCheck.put((grid[neighbourRow][neighbourColl], neighbourRow, neighbourColl))

        return grid[n - 1][n - 1]

    def neighbours(self, row, coll, n):
        neighbours = []
        if 0 <= row - 1:
            neighbours.append((row - 1, coll))
        if row + 1 < n:
            neighbours.append((row + 1, coll))
        if 0 <= coll - 1:
            neighbours.append((row, coll - 1))
        if coll + 1 < n:
            neighbours.append((row, coll + 1))

        return neighbours
    
if __name__ == "__main__":
    test = Solution()
    grid = [[0,2],[1,3]]
    print(test.swimInWater(grid))
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    print(test.swimInWater(grid))