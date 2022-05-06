#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

# @lc code=start
from typing import List


class RecentCounter:

    def __init__(self):
        self.t_list: List[int] = []
        self.count: int = 0

    def ping(self, t: int) -> int:
        for i in range(self.count, len(self.t_list)):
            if t - self.t_list[i] <= 3000:
                break
            self.count += 1
        self.t_list.append(t)
        return len(self.t_list) - self.count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# print(obj.ping(1), obj.ping(100), obj.ping(3001), obj.ping(3002))
# @lc code=end
