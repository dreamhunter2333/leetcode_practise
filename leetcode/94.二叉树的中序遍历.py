#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # res = []

        # def func(node):
        #     if not node:
        #         return
        #     if node.left:
        #         func(node.left)
        #     res.append(node.val)
        #     if node.right:
        #         func(node.right)
        # func(root)
        # return res

        # 非递归
        res = []
        if not root:
            return res
        node_list = []
        node = root
        while (node or node_list):
            while (node):
                node_list.append(node)
                node = node.left
            cur_node = node_list.pop()
            res.append(cur_node.val)
            node = cur_node.right
        return res

# @lc code=end
