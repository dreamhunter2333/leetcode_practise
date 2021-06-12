#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
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
        res = []
        stack = [root]
        while stack:
            stack_len = len(stack)
            if all(s is None for s in stack):
                break
            for _ in range(stack_len):
                node = stack.pop(0)
                if node:
                    res.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
                else:
                    res.append(None)

        return ','.join(map(str, res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        node_list = [None if d == 'None' else TreeNode(int(d)) for d in data.split(',')]
        head = node_list.pop(0)
        stack = [head]
        while node_list:
            stack_len = len(stack)
            for _ in range(stack_len):
                node = stack.pop(0)
                if not node:
                    continue
                node.left = node_list.pop(0)
                node.right = node_list.pop(0)
                stack.append(node.left)
                stack.append(node.right)

        return head


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
