from typing import List, Optional
from heapq import heapify, heappop, heappush

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # guardian
        merged_list = ListNode()
        merged_list_tail = merged_list
        lists_heads = [node for node in lists if node is not None]

        heap = [(node.val, list_head_idx) for list_head_idx, node in enumerate(lists_heads)]
        heapify(heap)

        while heap:
            _, list_head_idx = heappop(heap)


            node = lists_heads[list_head_idx]
            next_node: Optional[ListNode] = node.next
            lists_heads[list_head_idx] = next_node
            node.next = None

            if next_node is not None:
                heappush(heap, (next_node.val, list_head_idx))

            merged_list_tail.next = node
            merged_list_tail = node

        return merged_list.next

def print_list(head: Optional[ListNode]) -> None:
    while head is not None:
        print(f"{head.val} -> ", end="")
        head = head.next

    print("end")

if __name__ == "__main__":
    sol = Solution()

    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ]

    node = sol.mergeKLists(lists)
    print_list(node)

