class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            #end if
        #end while
        fast = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        #end while
        return slow
    
if __name__ == "__main__":
    object = Solution
    nums = [1,3,4,2,2]
    print(object.findDuplicate(object, nums))
    nums = [3,1,3,4,2]
    print(object.findDuplicate(object, nums))