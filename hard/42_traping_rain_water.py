class Solution:
    def trap(self, height: list[int]) -> int:
        beg = 0
        end = len(height) - 1
        if end - beg < 2:
            return 0
        
        waterLevel = min(height[beg], height[end])
        waterSum = (end - beg - 1) * waterLevel

        while beg + 1 < end:
            print(f"water level: {waterLevel}, water sum: {waterSum} (before updating)")
            # update pointers
            updatedPtr = beg + 1
            notUpdatedPtr = end
            if height[beg] <= height[end]:
                beg += 1
            else:
                end -= 1
                updatedPtr = end
                notUpdatedPtr = beg
            
            if height[updatedPtr] > waterLevel:
                waterSum -= waterLevel
                newLevel = min(height[updatedPtr], height[notUpdatedPtr])
                if newLevel > waterLevel:
                    waterSum += (end - beg - 1) * (newLevel - waterLevel)
                    waterLevel = newLevel
            else:
                waterSum -= height[updatedPtr]

            print(f"beg: {beg}, end: {end}")
            print(f"water level: {waterLevel}, water sum: {waterSum} (after update)")
        
        return waterSum
    
if __name__ == "__main__":
    test = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"result: {test.trap(height)}")
    height = [4,2,0,3,2,5]
    print()
    print(f"result: {test.trap(height)}")

