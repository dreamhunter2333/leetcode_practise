#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        node_list = [root]
        while (len(node_list)):
            res.append(
                sum(node.val for node in node_list)/len(node_list)
            )
            new_list = []
            for node in node_list:
                if node.left:
                    new_list.append(node.left)
                if node.right:
                    new_list.append(node.right)
            node_list = new_list
        return res

# @lc code=end
