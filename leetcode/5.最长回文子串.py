#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩展算法

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start, end = 0, 0

        for i in range(len(s)):
            # 单数
            left1, right1 = expandAroundCenter(i, i)
            # 双数
            left2, right2 = expandAroundCenter(i, i + 1)
            # 更新最大回文子串
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

# @lc code=end
