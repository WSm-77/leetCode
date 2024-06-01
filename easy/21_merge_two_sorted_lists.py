# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resultList = ListNode()
        last = resultList

        while list1 != None and list2 != None:
            if list2.val < list1.val:
                last.next = list2
                list2 = list2.next
            else:
                last.next = list1
                list1 = list1.next
            
            last = last.next

        if list1 == None:
            list1 = list2
            
        while list1 != None:
            last.next = list1
            list1 = list1.next
            last = last.next

        return resultList.next