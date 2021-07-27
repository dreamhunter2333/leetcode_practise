#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res1 = float('inf')
        res2 = float('inf')

        stack = [root]

        while stack:
            node = stack.pop(0)
            if not node:
                continue
            if res2 > node.val:
                res1 = res2
                res2 = node.val
            elif res1 > node.val > res2:
                res1 = node.val
            elif node.val >= res1:
                continue
            stack.append(node.left)
            stack.append(node.right)
        return res1 if res1 != float('inf') else -1

# @lc code=end
