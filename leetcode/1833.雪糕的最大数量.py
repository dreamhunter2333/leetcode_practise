#
# @lc app=leetcode.cn id=1833 lang=python3
#
# [1833] 雪糕的最大数量
#

# @lc code=start
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        res = 0

        for c in costs:
            if coins >= c:
                coins -= c
                res += 1
            else:
                break

        return res


# @lc code=end
