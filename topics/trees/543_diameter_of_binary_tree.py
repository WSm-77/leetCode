# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def rek(node):
            if node is None:
                return 0, 0
            
            maxDiamLeft, maxLeftPath = rek(node.left)
            maxDiamRight, maxRightPath = rek(node.right)

            return max(maxDiamLeft, maxDiamRight, maxLeftPath + maxRightPath), max(maxRightPath, maxLeftPath) + 1
        #end def

        result, _ = rek(root)
        
        return result