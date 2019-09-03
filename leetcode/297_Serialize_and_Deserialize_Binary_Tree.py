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
        lc_tree = [root.val]
        # root is at level 1, root has only one item at the same level
        # when level=2, max_items = 2^(level-1)
        level = 1
        next = []
        fin = False

        while fin is False:
            current = next
            next = []
            has_next = False
            i, node = 0, 0
            while i < 2 ** (level - 1) or has_next is False:
                if current:
                    root = current[i]
                if self.get_next_level(root)[0] != 0:
                    has_next = True
                i += 1

            if has_next is True:
                for i in range(0, 2 ** (level - 1)):

                    if current:
                        root = current[i]
                    if self.get_next_level(root)[0] != 0:
                        for item in self.get_next_level(root)[1]:
                            next.append(item)
                            lc_tree.append(item.val)
                    else:
                        lc_tree.append(None)
                        lc_tree.append(None)
            level += 1

            print(level, lc_tree)

            for x in next:
                if x.left == None and x.right == None:
                    node += 1
            if node == len(next):
                fin = True
        return lc_tree


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))