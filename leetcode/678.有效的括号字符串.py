#
# @lc app=leetcode.cn id=678 lang=python3
#
# [678] 有效的括号字符串
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        count_left = []
        count_x = []

        for i, c in enumerate(s):
            if c == '(':
                count_left.append(i)
            elif c == '*':
                count_x.append(i)
            elif c == ')' and count_left:
                count_left.pop()
            elif c == ')' and count_x:
                count_x.pop()
            else:
                return False

        while count_left and count_x:
            if count_left.pop() > count_x.pop():
                return False

        return len(count_left) == 0

# @lc code=end
