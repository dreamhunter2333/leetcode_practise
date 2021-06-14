#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:

        def dfs(node):
            if not node:
                return 0, 0
            l_res1, l_res2 = dfs(node.left)
            r_res1, r_res2 = dfs(node.right)
            return r_res2 + l_res2 + node.val, max(l_res1, l_res2) + max(r_res1, r_res2)

        return max(dfs(root))

# @lc code=end
