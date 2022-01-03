#
# @lc app=leetcode.cn id=1185 lang=python3
#
# [1185] 一周中的第几天
#

# @lc code=start
# import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        # return datetime.date(year, month, day).strftime('%A')

        res = [
            "Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"
        ]
        # 1971-1-1 为 Friday
        day += 5

        def is_leap(y):
            return (
                y % 4 == 0 and y % 100 != 0
            ) or (
                y % 400 == 0 and y % 3200 != 0
            ) or y % 172800 == 0

        for y in range(1971, year):
            day += (366 if is_leap(y) else 365)

        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap(year):
            month_days[1] = 29
        day += sum(month_days[:month - 1])

        return res[day % 7 - 1]


# print(Solution().dayOfTheWeek(day=15, month=8, year=1993))
# @lc code=end
