#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (32.02%)
# Likes:    2729
# Dislikes: 0
# Total Accepted:    275K
# Total Submissions: 858.6K
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
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
# @lc code=end

