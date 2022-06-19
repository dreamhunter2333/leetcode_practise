#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:

        cache = defaultdict(int)

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            res_left = dfs(node.left)
            res_right = dfs(node.right)
            sum_node = res_left + node.val + res_right
            cache[sum_node] += 1
            return sum_node

        dfs(root)
        max_count = max(cache.values())
        return [
            s for s, count in cache.items()
            if count == max_count
        ]


# @lc code=end
