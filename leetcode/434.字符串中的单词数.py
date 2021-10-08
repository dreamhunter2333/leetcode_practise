#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        res = 0
        count_flag = True
        for c in s:
            isalp = c != " "
            if count_flag and isalp:
                res += 1
                count_flag = False
            elif not isalp:
                count_flag = True

        return res

# @lc code=end
