#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # res = True

        # def dfs(node):
        #     nonlocal res
        #     if not node:
        #         return float('-inf'), float('inf')

        #     left_max, left_min = dfs(node.left)
        #     right_max, right_min = dfs(node.right)

        #     if left_max >= node.val or node.val >= right_min:
        #         res = False
        #         return float('inf'), float('-inf')

        #     return max(
        #         left_max, right_max, node.val
        #     ), min(left_min, right_min, node.val)

        # dfs(root)

        # return res

        # 中序遍历
        stack = []
        last_val = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if node.val <= last_val:
                return False
            last_val = node.val
            root = node.right

        return True

# @lc code=end
