# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def get_next_level(self, root):
        # return the number of next level items, and a list [item1, item2]
        n = 0
        l = []
        if root.left:
            l.append(root.left)
            n += 1
        else:
            l.append("null")

        if root.right:
            l.append(root.right)
            n += 1
        else:
            l.append("null")
        return n, l

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        lc_tree, next = [root.val], [root, 0]
        # root is at level 1, root has only one item at the same level
        # when level=2, max_items = 2^(level-1)
        level = 1

        for i in range(0, 2**(level-1)):
            root = next[i]
            if self.get_next_level(root)[0] != 0:
                for i in self.get_next_level(root)[1]:
                    next.append(i)
                    lc_tree.append(i)

            level += 1


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))