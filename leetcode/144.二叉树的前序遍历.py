#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # res = []

        # def func(node):
        #     if not node:
        #         return
        #     res.append(node.val)
        #     func(node.left)
        #     func(node.right)
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
            if cur_node.right:
                node_list.append(cur_node.right)
            if cur_node.left:
                node_list.append(cur_node.left)
        return res

# @lc code=end
