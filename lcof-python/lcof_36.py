"""
剑指 Offer 36. 二叉搜索树与双向链表
# Definition for a Node.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if not root:
            return

        head_node = Node()
        cur_node = head_node

        def dfs(node):
            nonlocal cur_node
            if not node:
                return
            dfs(node.left)
            cur_node.right = node
            node.left = cur_node
            cur_node = node
            dfs(node.right)

        dfs(root)
        res = head_node.right
        if res:
            cur_node.right = res
            res.left = cur_node

        return res
