#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def dfs(node):
            nonlocal res
            if not node:
                return False
            left_res = dfs(node.left)
            right_res = dfs(node.right)
            if (
                left_res and right_res
            ) or (
                (node.val == p.val or node.val == q.val) and (left_res or right_res)
            ):
                res = node
            return left_res or right_res or node.val == p.val or node.val == q.val
        dfs(root)
        return res

# @lc code=end
