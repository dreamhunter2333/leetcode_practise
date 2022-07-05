#
# @lc app=leetcode.cn id=729 lang=python3
#
# [729] 我的日程安排表 I
#

# @lc code=start
class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        for start_day, end_day in self.booked:
            if start_day < end and start < end_day:
                return False
        self.booked.append((start, end))
        return True


# @lc code=end
# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10, 20), obj.book(15, 25), obj.book(20, 30))
