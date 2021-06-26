#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        flag = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and flag:
                break
            elif s[i] == ' ':
                continue
            else:
                flag = True
                res = res + 1
        return res

# @lc code=end
