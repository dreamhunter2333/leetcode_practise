#
# @lc app=leetcode.cn id=1817 lang=python3
#
# [1817] 查找用户活跃分钟数
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0] * k
        cache_map = defaultdict(set)
        for user, minute in logs:
            cache_map[user].add(minute)
        for minute_set in cache_map.values():
            res[len(minute_set) - 1] += 1
        return res
# @lc code=end
