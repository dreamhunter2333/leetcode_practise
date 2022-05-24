#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [root]
        val = root.val
        while stack:
            node = stack.pop()
            if node.val != val:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True


# @lc code=end
