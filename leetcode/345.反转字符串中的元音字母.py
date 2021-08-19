#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        char_set = set(list("aeiouAEIOU"))
        n = len(s)
        s = list(s)
        i, j = 0, n - 1
        while i < j:
            while i < n and s[i] not in char_set:
                i += 1
            while j > 0 and s[j] not in char_set:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)

# @lc code=end
