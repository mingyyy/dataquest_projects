# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def hasNext(self, root: TreeNode):
        counter = 0
        if root.left or root.right:
            return True
        else:
            return False

    def maxDepth(self, root: TreeNode) -> int:
        counter = 1
        while hasNext(root):
            counter += 1
            if not hasNext(root):
                return counter
            else:
                try:
                    root = root.left
                except:
                    root = root.right

