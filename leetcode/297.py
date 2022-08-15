# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "x"

        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return "[%s,%s,%s]" % (root.val, left, right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "x":
            return None

        data = data[1:-1]
        root = TreeNode(int(data[:data.index(",")]))

        data = data[data.index(",") + 1:]
        open_brackets = 0
        for i in range(len(data)):
            if data[i] == "," and open_brackets == 0:
                root.left = self.deserialize(data[:i])
                root.right = self.deserialize(data[i + 1:])
                break
            elif data[i] == "[":
                open_brackets += 1
            elif data[i] == "]":
                open_brackets -= 1
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))