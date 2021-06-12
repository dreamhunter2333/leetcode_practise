#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        def dfs(node, val_list):
            if not node:
                return 0

            for i in range(len(val_list)):
                val_list[i] += node.val
            val_list.append(node.val)

            left = dfs(node.left, val_list[:])
            right = dfs(node.right, val_list[:])

            return left + right + sum(1 for r in val_list if r == targetSum)

        return dfs(root, [])

# @lc code=end
