#
# @lc app=leetcode.cn id=2283 lang=python3
#
# [2283] 判断一个数的数字计数是否等于数位的值
#

# @lc code=start
from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        return num == "".join(
            str(c.get(str(i), "0"))
            for i in range(len(num))
        )


# @lc code=end
print(Solution().digitCount("1210"))
