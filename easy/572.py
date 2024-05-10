# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#######################
# iterative  solution #
#######################

from collections import deque

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return subRoot == None

        toCheck = deque()
        toCheck.append(root)

        while toCheck:
            node = toCheck.pop()

            if self.isSameTree(node, subRoot):
                return True

            if node.left != None:
                toCheck.append(node.left)

            if node.right != None:
                toCheck.append(node.right)

        return False

    def isSameTree(self, root1, root2):
        if root1 == root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False

        toCheck = deque()
        toCheck.append((root1, root2))

        result = True

        while toCheck:
            node1, node2 = toCheck.pop()

            if node1.val != node2.val:
                result = False
                break

            if node1.left != None:
                if node2.left == None:
                    result = False
                    break
                toCheck.append((node1.left, node2.left))
            else:
                if node2.left != None:
                    result = False
                    break

            if node1.right != None:
                if node2.right == None:
                    result = False
                    break
                toCheck.append((node1.right, node2.right))
            else:
                if node2.right != None:
                    result = False
                    break

        return result

#######################
# recursive  solution #
#######################

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def rek(root):
            nonlocal subRoot
            if self.isSameTree(root, subRoot):
                return True
            elif root == None:
                return False

            return rek(root.left) or rek(root.right)
        # end def
        return rek(root)

    def isSameTree(self, root1, root2):
        if root1 == root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False

        return root1.val == root2.val and self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)