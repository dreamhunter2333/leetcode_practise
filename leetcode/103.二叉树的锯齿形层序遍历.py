#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        stack = [root]
        reverse_order = False
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
                res.append(new_res[::-1] if reverse_order else new_res)
            reverse_order = not reverse_order
        return res


# @lc code=end
