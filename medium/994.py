from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        colls = len(grid[0])
        minutes = [[None for _ in range(colls)] for _ in range(rows)]
        # 0 - row, 1 - collumn
        queue = deque()
        neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        freshOrangesCnt = 0

        # find all rotten oranges
        for R in range(rows):
            for C in range(colls):
                if grid[R][C] == 2:         # this orange is rotten
                    queue.append((R, C))
                    minutes[R][C] = 0
                elif grid[R][C] == 1:       # this orrange is fresh
                    freshOrangesCnt += 1

        lastRotteningMinute = 0

        while queue:
            R, C = queue.popleft()
            for x, y in neighbours:
                newRow, newColl = R + x, C + y
                # if orange is not rotten in current minute update its rottening minute
                if (0 <= newRow < rows) and (0 <= newColl < colls) and grid[newRow][newColl] == 1:
                    minutes[newRow][newColl] = minutes[R][C] + 1
                    lastRotteningMinute = max(lastRotteningMinute, minutes[newRow][newColl])
                    
                    # mark orange rotten and add to queue
                    grid[newRow][newColl] = 2
                    queue.append((newRow, newColl))
                    freshOrangesCnt -= 1
                
        return lastRotteningMinute if freshOrangesCnt == 0 else -1



if __name__ == "__main__":
    test = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(test.orangesRotting(grid))

    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(test.orangesRotting(grid))

    grid = [[0,2]]
    print(test.orangesRotting(grid))