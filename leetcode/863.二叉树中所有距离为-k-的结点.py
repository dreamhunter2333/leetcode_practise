#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []

        def dfs(node, distance=None):
            if not node:
                return
            if node == target:
                distance = 0
            if distance == k:
                res.append(node.val)
                return
            if distance is None:
                res1 = dfs(node.left)
                if res1 == k:
                    res.append(node.val)
                elif res1:
                    dfs(node.right, res1 + 1)
                    return res1 + 1
                res2 = dfs(node.right)
                if res2 == k:
                    res.append(node.val)
                elif res2:
                    dfs(node.left, res2 + 1)
                    return res2 + 1
            else:
                dfs(node.left, distance + 1)
                dfs(node.right, distance + 1)
            return distance + 1 if distance is not None else distance

        dfs(root)

        return res


def list2node(nums: List[int], target: int) -> List[TreeNode]:
    root = TreeNode(nums.pop(0))
    target_node = None
    stack = [root]

    while stack:
        n = len(stack)
        for _ in range(n):
            node = stack.pop(0)
            if not node:
                continue
            if node.val == target:
                target_node = node
            if nums:
                val = nums.pop(0)
                node.left = TreeNode(val) if val is not None else None
                val = nums.pop(0)
                node.right = TreeNode(val) if val is not None else None
                stack.append(node.left)
                stack.append(node.right)
    return [root, target_node]


print(Solution().distanceK(
    *list2node([0, 1, None, 3, 2], 2),
    k=1
))
# @lc code=end
