#
# @lc app=leetcode.cn id=1609 lang=python3
#
# [1609] 奇偶树
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        odd = 1
        while stack:
            next_stack = []
            before = 0 if odd else float("inf")
            for node in stack:
                if node.val % 2 != odd or (
                    odd == 1 and before >= node.val
                ) or (
                    odd == 0 and before <= node.val
                ):
                    return False
                before = node.val
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            odd ^= 1
            stack = next_stack
        return True


# def list2node(nums) -> TreeNode:
#     root = TreeNode(nums.pop(0))
#     stack = [root]

#     while stack:
#         n = len(stack)
#         for _ in range(n):
#             node = stack.pop(0)
#             if not node:
#                 continue
#             val = nums.pop(0) if nums else None
#             node.left = TreeNode(val) if val is not None else None
#             val = nums.pop(0) if nums else None
#             node.right = TreeNode(val) if val is not None else None
#             stack.append(node.left)
#             stack.append(node.right)
#     return root


# print(Solution().isEvenOddTree(
#     list2node([5, 9, 1, 3, 5, 7])
# ))
# @lc code=end
