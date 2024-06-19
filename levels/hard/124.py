# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         def maxPath(node) -> tuple[bool, int, int]:
#             if node.right == node.left == None:
#                 return False, 0, node.val
            
#             nonEmptyRightPath, maxRightPath = False, -INF
#             maxSingleSidePath = -INF
#             if node.right != None:
#                 nonEmptyRightPath = True
#                 validRightPah, maxRightPath, maxPathInRightSubtree = maxPath(node.right)
#                 maxSingleSidePath = maxRightPath
#             nonEmptyLeftPath, maxLeftPath = False, -INF
#             if node.left != None:
#                 nonEmptyLeftPath = True
#                 validLeftPath, maxLeftPath, maxPathInLeftSubtree = maxPath(node.left)
#                 maxSingleSidePath = max(maxSingleSidePath, maxLeftPath)


#             maxDoubleSidePath = -INF
#             if nonEmptyRightPath:
#                 maxDoubleSidePath += maxRightPath
#             if nonEmptyLeftPath:
#                 maxDoubleSidePath += maxLeftPath

            

#             return True, maxSingleSidePath, 
#         #end def

#         INF = float("inf")
#         _, result = maxPath(root)

#         return result