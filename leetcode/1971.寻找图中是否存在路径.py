#
# @lc app=leetcode.cn id=1971 lang=python3
#
# [1971] 寻找图中是否存在路径
#

# @lc code=start
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if destination == source:
            return True
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for x, y in edges:
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                continue
            parent[root_y] = root_x

        return find(source) == find(destination)


# @lc code=end
print(Solution().validPath(
    n=3, edges=[[0, 1], [1, 2], [2, 0]],
    source=0, destination=2
))
print(Solution().validPath(
    n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]],
    source=0, destination=5
))
