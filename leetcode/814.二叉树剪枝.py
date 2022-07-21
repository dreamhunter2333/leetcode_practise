#
# @lc app=leetcode.cn id=814 lang=python3
#
# [814] 二叉树剪枝
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def dfs(node: TreeNode) -> bool:
            if not node:
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == 0 and left and right:
                return True
            if left:
                node.left = None
            if right:
                node.right = None
            return False

        return None if dfs(root) else root

# @lc code=end
