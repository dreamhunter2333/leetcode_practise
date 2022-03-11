#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(node: 'Node') -> None:
            if not node:
                return
            for children in node.children:
                dfs(children)
            res.append(node.val)

        dfs(root)
        return res

# @lc code=end
