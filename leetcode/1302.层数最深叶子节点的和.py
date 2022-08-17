#
# @lc app=leetcode.cn id=1302 lang=python3
#
# [1302] 层数最深叶子节点的和
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        stack = [root]

        while stack:
            new_stack = [
                child
                for node in stack
                if node
                for child in (node.left, node.right)
                if child
            ]
            if not new_stack:
                break
            stack = new_stack
        return sum(node.val for node in stack)
# @lc code=end
