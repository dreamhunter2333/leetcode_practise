#
# @lc app=leetcode.cn id=1305 lang=python3
#
# [1305] 两棵二叉搜索树中的所有元素
#

# @lc code=start
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []

        def dfs(node: TreeNode):
            if not node:
                return
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)

        node1_iter = dfs(root1)
        node2_iter = dfs(root2)

        num1 = num2 = None
        while True:
            try:
                num1 = next(node1_iter) if num1 is None else num1
                num2 = next(node2_iter) if num2 is None else num2
                if num1 >= num2:
                    res.append(num2)
                    num2 = None
                else:
                    res.append(num1)
                    num1 = None
            except StopIteration:
                if num1:
                    res.append(num1)
                if num2:
                    res.append(num2)
                break

        res.extend(node1_iter)
        res.extend(node2_iter)

        return res

# @lc code=end
