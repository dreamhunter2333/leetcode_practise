#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        stack = [root]
        while stack:
            stack_len = len(stack)
            new_res = []
            for _ in range(stack_len):
                node = stack.pop(0)
                if not node:
                    continue
                new_res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            if new_res:
                res.append(new_res)
        return res


# @lc code=end
