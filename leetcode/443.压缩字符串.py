#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#

# @lc code=start
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        pre = None
        count = 0
        for i in range(n):
            c = chars.pop(0)
            if c == pre:
                count += 1
                continue
            if count > 1:
                chars.extend(str(count))
            count = 1
            chars.append(c)
            pre = c

        if count > 1:
            chars.extend(str(count))

        return len(chars)

# @lc code=end
