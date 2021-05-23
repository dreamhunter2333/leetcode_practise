#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # res = []

        # def func(node):
        #     if not node:
        #         return
        #     func(node.left)
        #     func(node.right)
        #     res.append(node.val)
        # func(root)
        # return res

        # 非递归
        res = []
        if not root:
            return res
        node_list = [root]
        while (node_list):
            cur_node = node_list.pop()
            res.append(cur_node.val)
            if cur_node.left:
                node_list.append(cur_node.left)
            if cur_node.right:
                node_list.append(cur_node.right)
        return res[::-1]

# @lc code=end
