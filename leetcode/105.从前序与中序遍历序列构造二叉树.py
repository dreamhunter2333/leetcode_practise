#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return

        def find_root(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right or in_left > in_right:
                return
            item = preorder[pre_left]
            in_root = inorder.index(item)
            left_count = in_root - in_left

            new_node = TreeNode(item)
            new_node.left = find_root(pre_left+1, pre_left+left_count, in_left, in_root-1)
            new_node.right = find_root(pre_left+left_count+1, pre_right, in_root+1, in_right)

            return new_node

        return find_root(0, len(preorder) - 1, 0, len(inorder) - 1)


def aaa(root):
    res = []
    stack = [root]
    while stack:
        stack_len = len(stack)
        for _ in range(stack_len):
            node = stack.pop(0)
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

    print(res)


aaa(Solution().buildTree(
    preorder=[3, 9, 20, 15, 7],
    inorder=[9, 3, 15, 20, 7]
))
# @lc code=end
