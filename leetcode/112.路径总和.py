#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        res = []
        path = []

        def dfs(node, val, cur_path):
            if not node:
                return True
            val += node.val
            cur_path.append(node.val)
            res1 = dfs(node.left, val, cur_path)
            res2 = dfs(node.right, val, cur_path)
            if res1 and res2 and val == targetSum:
                res.append(cur_path[:])
            cur_path.pop()

        dfs(root, 0, path)

        return True if res else False

# @lc code=end
