# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        prevRoot = root
        alternateWay = root.right
        root = root.left
        while True:
            inTheTreeCnt = self.in_the_tree_cnt(root, p, q)
            if inTheTreeCnt == 1:
                break
            elif inTheTreeCnt == 2:
                prevRoot = root
                alternateWay = root.right
                root = root.left
            else:
                root = alternateWay
        # end while

        return prevRoot

    def in_the_tree_cnt(self, root, p, q):
        def rek(root):
            nonlocal p, q
            if root == None:
                return 0

            correction = 0
            if root == p or root == q:
                correction = 1

            return rek(root.left) + rek(root.right) + correction
        # end def
        return rek(root)