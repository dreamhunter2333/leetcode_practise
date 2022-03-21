#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        cahce_set = set()
        nodes = [root]

        while nodes:
            new_nodes = []
            for node in nodes:
                if not node:
                    continue
                if node.val in cahce_set:
                    return True
                cahce_set.add(k - node.val)
                new_nodes.append(node.left)
                new_nodes.append(node.right)
            nodes = new_nodes

        return False

# @lc code=end
