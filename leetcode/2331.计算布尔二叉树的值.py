#
# @lc app=leetcode.cn id=2331 lang=python3
#
# [2331] 计算布尔二叉树的值
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> bool:
            match node.val:
                case 1: return True
                case 2: return dfs(node.left) or dfs(node.right)
                case 3: return dfs(node.left) and dfs(node.right)
                case _: return False
        return dfs(root)
# @lc code=end
