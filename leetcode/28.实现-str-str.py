#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if not needle:
            return 0
        if not haystack or m > n:
            return -1

        for i in range(n-m+1):
            flag = True
            for j in range(m):
                if haystack[i+j] != needle[j]:
                    flag = False
                    break
            if flag:
                return i

        return -1

# @lc code=end
