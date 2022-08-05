#
# @lc app=leetcode.cn id=623 lang=python3
#
# [623] 在二叉树中增加一行
#

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return root
        if depth == 1:
            return TreeNode(val=val, left=root)
        nodes = [root]
        while depth > 2:
            depth -= 1
            nodes = [
                target
                for node in nodes if node
                for target in (node.left, node.right)
                if target
            ]
        for node in nodes:
            new_node_left = TreeNode(val=val, left=node.left)
            new_node_right = TreeNode(val=val, right=node.right)
            node.left = new_node_left
            node.right = new_node_right
        return root
# @lc code=end
