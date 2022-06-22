#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            raise
        res = None
        node_list = [root]
        while (len(node_list)):
            res = node_list[0].val
            new_list = []
            for node in node_list:
                if node.left:
                    new_list.append(node.left)
                if node.right:
                    new_list.append(node.right)
            node_list = new_list
        return res

# @lc code=end
