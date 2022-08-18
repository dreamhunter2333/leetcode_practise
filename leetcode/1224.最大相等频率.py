#
# @lc app=leetcode.cn id=1224 lang=python3
#
# [1224] 最大相等频率
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq, count = defaultdict(int), defaultdict(int)
        ans = maxFreq = 0
        for i, num in enumerate(nums):
            if count[num]:
                freq[count[num]] -= 1
            count[num] += 1
            maxFreq = max(maxFreq, count[num])
            freq[count[num]] += 1
            if (
                maxFreq == 1 or
                freq[maxFreq] * maxFreq + freq[maxFreq - 1] * (maxFreq - 1) == i + 1 and freq[maxFreq] == 1 or
                freq[maxFreq] * maxFreq + 1 == i + 1 and freq[1] == 1
            ):
                ans = max(ans, i + 1)
        return ans

# @lc code=end
