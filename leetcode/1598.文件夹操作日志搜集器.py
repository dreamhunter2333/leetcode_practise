#
# @lc app=leetcode.cn id=1598 lang=python3
#
# [1598] 文件夹操作日志搜集器
#
from typing import List


# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for log_item in logs:
            if log_item == "../":
                if level > 0:
                    level -= 1
            elif log_item != "./":
                level += 1
        return level

# @lc code=end
