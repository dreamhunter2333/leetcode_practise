#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(c.lower() for c in s if c.isalnum())
        new_s_len = len(new_s)
        for i in range(new_s_len // 2):
            if new_s[i] != new_s[new_s_len - i - 1]:
                return False
        return True

# @lc code=end
