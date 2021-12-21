#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#
# https://leetcode-cn.com/problems/day-of-the-year/description/
#

# @lc code=start


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day_total = map(int, date.split('-'))
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 3200 != 0) or year % 172800 == 0:
            month_days[1] = 29
        day_total += sum(month_days[:month - 1])

        return day_total


# print(Solution().dayOfYear("1969-09-28"))
# @lc code=end
