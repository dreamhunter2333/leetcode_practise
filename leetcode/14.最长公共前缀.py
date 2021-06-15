#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = strs.pop()
        for s in strs:
            if not res:
                return res
            new_res = ""
            for i in range(min(len(s), len(res))):
                if s[i] != res[i]:
                    break
                new_res += res[i]
            res = new_res
        return res

# @lc code=end
