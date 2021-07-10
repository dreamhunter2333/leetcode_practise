#
# @lc app=leetcode.cn id=981 lang=python3
#
# [981] 基于时间的键值存储
#

# @lc code=start
from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        data = self.data[key]
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        return self.data[key][right][0] if right >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
