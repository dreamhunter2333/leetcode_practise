#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#
from typing import List
# @lc code=start


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        n = len(strs[0])
        m = len(strs)
        for i in range(n):
            for j in range(1, m):
                if strs[j][i] >= strs[j-1][i]:
                    continue
                res += 1
                break
        return res


# @lc code=end
print(Solution().minDeletionSize(["rrjk", "furt", "guzm"]))
