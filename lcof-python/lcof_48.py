# -*- coding: utf-8 -*-
"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        # 滑动窗口
        char_set = set()
        left = 0
        cur_len = 0
        max_len = 0

        for i in range(len(s)):
            cur_len += 1
            while s[i] in char_set:
                char_set.remove(s[left])
                left += 1
                cur_len -= 1
            max_len = max(cur_len, max_len)
            char_set.add(s[i])

        return max_len


print(Solution().lengthOfLongestSubstring("pwwkew"))
