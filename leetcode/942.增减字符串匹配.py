#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#

# @lc code=start
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        start = 0
        end = len(s)
        for c in s:
            if c == "I":
                res.append(start)
                start += 1
            else:
                res.append(end)
                end -= 1
        res.append(end)
        return res


# print(Solution().diStringMatch("IDID"))
# print(Solution().diStringMatch("III"))
# print(Solution().diStringMatch("DDI"))
# @lc code=end
