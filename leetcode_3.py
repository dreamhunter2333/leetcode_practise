# -*- coding: utf-8 -*-

"""
3. 无重复字符的最长子串

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        on = set()
        on_len = 0
        max_len = 0
        for index in range(len(s)):
            on_len += 1
            while s[index] in on:
                # 移出左侧的字符直到没有重复
                on.remove(s[left])
                left += 1
                on_len -= 1
            if on_len > max_len:max_len = on_len
            on.add(s[index])
        return max_len


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring('abccccccddddacc'))