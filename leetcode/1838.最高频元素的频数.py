#
# @lc app=leetcode.cn id=1838 lang=python3
#
# [1838] 最高频元素的频数
#

# @lc code=start
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        res = 1
        left = 0
        right = 1
        total = 0
        while left < right < n:
            length = right - left + 1
            total = nums[right] * length - (
                prefix_sum[right+1] - prefix_sum[left]
            )
            if total > k:
                left += 1
            else:
                res = max(res, length)
            right += 1

        return res


# @lc code=end
