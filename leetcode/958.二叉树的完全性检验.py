#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] 二叉树的完全性检验
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # 层序遍历，None 节点后面有非空节点即不完全
        # stack = [root]
        # have_null = False
        # while stack:
        #     node = stack.pop(0)
        #     if not node:
        #         have_null = True
        #         continue
        #     if have_null:
        #         return False
        #     stack.append(node.left)
        #     stack.append(node.right)
        # return True

        # 递归判断 树高
       res = True
        def dfs(node):
            nonlocal res
            if not node:
                return 0, 0
            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)
            if not any([(
                # 左侧树高和右侧最大树高相同
                left_max == left_min == right_max
                and right_max in (right_min, right_min+1)
            ), (
                # 左侧最小树高和右侧树高相同
                left_min == right_min == right_max
                and left_max in (left_min, left_min+1)
            ), (
                # 左侧树高 等于 右侧 +1
                left_max == left_min == right_min + 1 == right_max + 1
            )]):
                res = False
            return min(left_min, right_min)+1, max(left_max, right_max)+1

        dfs(root)
        return res


# @lc code=end
