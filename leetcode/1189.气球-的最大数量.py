#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_map = {c: 0 for c in "balloon"}
        for c in text:
            if c in count_map:
                count_map[c] += 1
        return min(
            num // 2 if c in "lo" else num
            for c, num in count_map.items()
        )


# print(Solution().maxNumberOfBalloons("nlaebolko"))
# @lc code=end
