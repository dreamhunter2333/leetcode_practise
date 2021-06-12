#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            res = max(left_sum + node.val + right_sum, res)

            return max(left_sum + node.val, right_sum + node.val, node.val, 0)

        dfs(root)

        return res


# @lc code=end
