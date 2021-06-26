#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(reversed(s.split()))
        res = []
        word = ''
        for c in s:
            if c == ' ' and word:
                res.append(word)
                word = ''
            elif c != ' ':
                word += c

        if word:
            res.append(word)

        return ' '.join(reversed(res))

# @lc code=end
