#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        cache_set = set()
        cache_set_len = 0
        max_len = 0
        for char in s:
            while char in cache_set:
                # 移出左侧的字符直到没有重复
                cache_set.remove(s[left])
                left += 1
                cache_set_len -= 1
            cache_set.add(char)
            cache_set_len += 1
            max_len = max(max_len, cache_set_len)
        return max_len


# @lc code=end
print(Solution().lengthOfLongestSubstring('abccccccddddacc'))
