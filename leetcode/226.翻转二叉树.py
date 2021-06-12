#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]

        while stack:
            stack_len = len(stack)
            for _ in range(stack_len):
                node = stack.pop(0)
                if not node:
                    continue
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root

# @lc code=end
