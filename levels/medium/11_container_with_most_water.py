class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        beg = 0
        end = n - 1

        result = 0
        while beg < end:
            minHeight = height[beg]
            width = end - beg
            if height[beg] < height[end]:
                beg += 1
            else:
                minHeight = height[end]
                end -= 1
            result = max(result, width*minHeight)

        return result