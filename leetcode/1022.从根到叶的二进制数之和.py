#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node: TreeNode, num: int):
            nonlocal res
            if not node:
                return
            num = num * 2 + node.val
            if not (node.left or node.right):
                res += num
                return
            dfs(node.left, num)
            dfs(node.right, num)

        dfs(root, 0)

        return res

# @lc code=end
