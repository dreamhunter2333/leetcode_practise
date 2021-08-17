#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        count_a = 0
        count_l = 0
        for c in s:
            if c == "L" and count_l > 1:
                return False
            if c == 'A' and count_a > 0:
                return False
            if c == 'A':
                count_a += 1
                count_l = 0
            elif c == "L":
                count_l += 1
            else:
                count_l = 0
        return True

# @lc code=end
