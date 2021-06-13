#
# @lc app=leetcode.cn id=987 lang=python3
#
# [987] 二叉树的垂序遍历
#

# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        cache = defaultdict(lambda: defaultdict(list))

        def dfs(node, col, row):
            if not node:
                return
            cache[col][row].append(node.val)
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0)

        res = []
        for col in sorted(cache):
            new_res = []
            for row in sorted(cache[col]):
                new_res.extend(sorted(cache[col][row]))
            res.append(new_res)
        return res

# @lc code=end
