#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
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
    def findTilt(self, root: TreeNode) -> int:
        res = 0

        def dfs(node: TreeNode) -> int:
            nonlocal res
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            res += abs(left_sum - right_sum)
            return left_sum + node.val + right_sum

        dfs(root)

        return res


def list_2_node(node_list: List[int]) -> TreeNode:
    root = TreeNode(val=node_list.pop(0))
    nodes = [root]
    while node_list:
        new_nodes = []
        for node in nodes:
            if not node:
                continue
            val = node_list.pop(0) if node_list else None
            node.left = TreeNode(
                val=val
            ) if val is not None else None
            val = node_list.pop(0) if node_list else None
            node.right = TreeNode(
                val=val
            ) if val is not None else None
            new_nodes.extend([node.left, node.right])
        nodes = new_nodes
    return root


print(Solution().findTilt(list_2_node([21, 7, 14, 1, 1, 2, 2, 3, 3])))
# @lc code=end
