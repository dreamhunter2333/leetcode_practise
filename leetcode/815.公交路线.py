#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] 公交路线
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        n = len(routes)
        dp = [set() for _ in range(n)]
        source_stack = []
        target_stack = []
        for i in range(n):
            for j in range(i + 1, n):
                if not set(routes[i]) & set(routes[j]):
                    continue
                dp[i].add(j)
                dp[j].add(i)
            if source in routes[i]:
                source_stack.append((i, 1))
            if target in routes[i]:
                target_stack.append(i)

        cache = set()

        while source_stack:
            cur, count = source_stack.pop(0)
            if cur in cache:
                continue
            cache.add(cur)
            if cur in target_stack:
                return count
            source_stack.extend([(d, count+1) for d in dp[cur]])

        return -1


print(Solution().numBusesToDestination(
    [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12))
# @lc code=end
