from typing import List

import heapq

##################
# first solution #
##################

# O(n + k * log n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)

        return -nums[0]

###################
# second solution #
###################

# theoretical O(n), but slow in practice

class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, len(nums) - k)

    def quick_select(self, arr: List[int], position: int) -> int:
        beg = 0
        end = len(arr) - 1

        while beg <= end:
            pivot = self.partition(arr, beg, end)

            if pivot == position:
                return arr[pivot]
            elif pivot < position:
                beg = pivot + 1
            else:
                end = pivot - 1

    def partition(self, arr: List, beg: int, end: int) -> int:
        pivot = beg

        for idx in range(beg, end):
            if arr[idx] < arr[end]:
                arr[pivot], arr[idx] = arr[idx], arr[pivot]
                pivot += 1

        arr[pivot], arr[end] = arr[end], arr[pivot]

        return pivot

def verify(expected: int, sol: Solution, sol2: Solution2, nums: List[int], k: int):
    output = sol.findKthLargest(nums, k)
    output2 = sol.findKthLargest(nums, k)

    assert output == output2
    assert output == expected

    print(output)

if __name__ == "__main__":
    sol = Solution()
    sol2 = Solution2()

    nums = [3,2,1,5,6,4]
    k = 2
    verify(5, sol, sol2, nums, k)

    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    verify(4, sol, sol2, nums, k)
