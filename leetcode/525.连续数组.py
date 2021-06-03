#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#

# @lc code=start
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_cache = 0
        cache_map = {1: -1}
        max_len = 0
        for i in range(len(nums)):
            sum_cache = sum_cache + nums[i]
            # 具有相同数量0和1的最长连续子数组
            # 即 sum(nums[:i]) sum(nums[:j]) = (i - j) / 2
            # 即 2 * sum - i 有相同值
            cache = 2 * sum_cache - i
            if cache in cache_map:
                max_len = max(i-cache_map[cache], max_len)
            else:
                cache_map[cache] = i
        return max_len


# @lc code=end
