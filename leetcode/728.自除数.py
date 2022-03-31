#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def is_self_dividing(num) -> bool:
            origin_num = num
            while num:
                target = num % 10
                if target == 0 or origin_num % target:
                    return False
                num = num // 10
            return True

        return [
            i
            for i in range(left, right + 1)
            if is_self_dividing(i)
        ]


# print(Solution().selfDividingNumbers(1, 22))
# @lc code=end
