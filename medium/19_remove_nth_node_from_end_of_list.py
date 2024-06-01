# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        guardian = ListNode(0, head)
        ptr = guardian

        for _ in range(n):
            head = head.next
        
        while head != None:
            head = head.next
            ptr = ptr.next
        
        ptr.next = ptr.next.next

        return guardian.next